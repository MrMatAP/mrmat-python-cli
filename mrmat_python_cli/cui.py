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
import cli_ui

from mrmat_python_cli import __version__
from mrmat_python_cli.commands import GreetingCommand, UIDemoCommand


def main() -> int:
    """
    Main entry point for the CLI

    :return: Exit code
    """
    parser = argparse.ArgumentParser(description=f'mrmat-python-cli-cui - {__version__}')  # NOSONAR
    parser.add_argument('-q', '--quiet', action='store_true', dest='quiet', help='Silent operation')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Debug')
    command_parser = parser.add_subparsers(help='Commands', dest='command')
    greeting_parser = command_parser.add_parser('greeting', help='Execute the greeting command')
    greeting_parser.add_argument('-n', '--name',
                                 dest='name',
                                 required=False,
                                 default='World',
                                 help='Name to greet (defaults to "World"')
    greeting_parser.set_defaults(func=GreetingCommand.execute)

    ui_demo_parser = command_parser.add_parser('ui-demo', help='UI Demo')
    ui_demo_parser.set_defaults(func=UIDemoCommand.execute)

    #
    # Parse arguments and initialise

    args = parser.parse_args()
    cli_ui.setup(verbose=args.debug, quiet=args.quiet, timestamp=False)

    #
    # Execute
    # Show help if no command was selected

    if args.command is None:
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
