#  MIT License
#
#  Copyright (c) 2022 Mathieu Imfeld
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

"""
Implementation of token acquisition with device code flow
"""

from commands import AbstractCommand
from mrmat_python_cli import console
import requests
import time
from datetime import datetime, timezone, timedelta
from rich.progress import Progress


class OpenIDRSTokenCommand(AbstractCommand):
    """
    A command to obtain an OpenID token via device code flow
    """

    def __call__(self) -> int:

        #
        # Obtain well-known IDP configuration

        resp = requests.get(self._args.well_known)
        if not resp.ok:
            console.print('Error while getting IDP well-known configuration')
            return 1
        well_known = resp.json()
        device_authorization_endpoint = well_known.get('device_authorization_endpoint')
        if not device_authorization_endpoint:
            console.print('There is no device authorization endpoint in the IDP')
            return 1
        token_endpoint = well_known.get('token_endpoint')
        if not token_endpoint:
            console.print('There is no token endpoint in the IDP')
            return 1

        #
        # Device Authorization Request
        # See https://datatracker.ietf.org/doc/html/rfc8628 Chapter 3.1

        data = dict(client_id=self._args.client_id)
        if self._args.scope:
            data['scope'] = self._args.scope
        resp = requests.post(url=device_authorization_endpoint,
                             headers={'Content-Type': 'application/x-www-form-urlencoded'},
                             data=data)
        if not resp.ok:
            console.print('Error during device authorization request')
        device_authorization = resp.json()
        console.print(f'Visit {device_authorization.get("verification_uri")} and type in '
                      f'{device_authorization.get("user_code")} or just visit '
                      f'{device_authorization.get("verification_uri_complete")}')
        expiry = datetime.now(tz=timezone.utc) + timedelta(seconds=device_authorization.get('expires_in'))
        done = False
        tokens = {}
        with Progress(transient=True) as progress:
            task = progress.add_task('Checking for authorisation...', total=device_authorization.get('expires_in'))
            while datetime.now(tz=timezone.utc) < expiry and not done:
                time.sleep(device_authorization.get('interval'))
                progress.update(task, advance=device_authorization.get('interval'))
                resp = requests.post(url=token_endpoint,
                                     headers={'Content-Type': 'application/x-www-form-urlencoded'},
                                     data=dict(
                                         grant_type='urn:ietf:params:oauth:grant-type:device_code',
                                         device_code=device_authorization.get('device_code'),
                                         client_id=self._args.client_id))
                if resp.ok:
                    done = True
                    tokens = resp.json()
            if not done:
                console.print('Token request has expired, please try again later')
                return 1
        console.print('Authorisation granted:')
        console.print_json(data=tokens)

        return 0
