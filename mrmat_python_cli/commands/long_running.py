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

"""A long running command class
"""

import time
from halo import Halo
import cli_ui

from mrmat_python_cli.commands import AbstractCommand


class LongRunningCommand(AbstractCommand):

    """A long running command class
    """

    done: bool = False

    def spinner(self) -> None:
        """
        Display dots in a separate thread during a long-running operation
        """
        while not self.done:
            cli_ui.dot()
            time.sleep(0.2)

    @Halo(text="I'm going to take a while", spinner='dots')
    def execute(self) -> int:
        """
        A long-running operation.
        By default we are using the Halo library to render a spinner. A simple alternative when it is not
        available:
            spinner_thread = Thread(name='spinner', target=self.spinner)
            spinner_thread.start()

            # Do some lengthy code here
            self.done = True

            cli_ui.dot(last=True)
        :return: Exit code
        """
        for _ in range(0, 5):
            # Do some lengthy work here
            time.sleep(1)
        self.done = True

        cli_ui.info('\nDone, 🦄')

        return 0
