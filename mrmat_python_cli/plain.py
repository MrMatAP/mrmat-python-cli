#  MIT License
#
#  Copyright (c) 2021 Mathieu Imfeld
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

import sys
import argparse
import logging

from mrmat_python_cli import __version__

logging.basicConfig(level=logging.WARNING, format='%(levelname)-8s - %(message)s')
LOG = logging.getLogger(__name__)


def main() -> int:
    """
    Main entry point for the CLI

    :return: Exit code
    """
    parser = argparse.ArgumentParser(description=f'mrmat-python-cli - {__version__}')
    parser.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='Be verbose')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Debug')

    args = parser.parse_args()
    if args.verbose:
        LOG.setLevel(logging.INFO)
    if args.debug:
        LOG.setLevel(logging.DEBUG)
        LOG.debug('Debug logging enabled')

    LOG.warning('Hello World!')
    return 0


if __name__ == '__main__':
    sys.exit(main())
