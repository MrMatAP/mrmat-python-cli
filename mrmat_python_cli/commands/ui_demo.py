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

import time
import cli_ui

from mrmat_python_cli.commands import AbstractCommand


class UIDemoCommand(AbstractCommand):

    def execute(self) -> int:
        cli_ui.info_section('Messages')
        cli_ui.info('This is an info message')
        cli_ui.info_1('This is an important informative message')
        cli_ui.info_2('This is a not so important informative message')
        cli_ui.info_3('This is an even less important informative message')
        cli_ui.warning('This is a warning message (on stderr)')
        cli_ui.error('This is an error message (on stderr)')
        # cli_ui.fatal('This is a fatal message (on stderr, exits)')
        cli_ui.debug(cli_ui.purple, 'This is a debug message')

        cli_ui.info_section('Formatting')
        cli_ui.info("one", "\n",
                    cli_ui.tabs(1), "two", "\n",
                    cli_ui.tabs(2), "three", "\n",
                    sep="")

        cli_ui.info_section('Table')
        headers = ['foo', 'bar', 'baz']
        data = [
            [(cli_ui.bold, '1'), (cli_ui.yellow, '2'), (cli_ui.purple, '3')],
            ['one', 'two', (cli_ui.cross, '')]
        ]
        cli_ui.info_table(data, headers=headers)

        cli_ui.info_section('Simple Progress')
        for i in range(0, 5):  # NOSONAR
            time.sleep(0.2)
            cli_ui.dot()
        cli_ui.dot(last=True)

        cli_ui.info_section('Labelled Progress')
        for i in range(0, 5):
            time.sleep(0.2)
            cli_ui.info_count(i, 5, 'Processing...')

        cli_ui.info_section('Percent Progress')
        for i in range(0, 5):
            time.sleep(0.2)
            cli_ui.info_progress("Processing", i, 5)

        return 0
