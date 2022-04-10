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

"""Main entry point for the Python CLI implementation
"""

import os
import sys
from configparser import ConfigParser
from typing import List, Optional
from argparse import ArgumentParser, Namespace
import cli_ui

from mrmat_python_cli import __version__
from mrmat_python_cli.commands import (
    GreetingCommand,
    UIDemoCommand,
    LongRunningCommand,
    ConfigShowCommand)


def parse_args(argv: List[str]) -> Optional[Namespace]:
    """A dedicated function to parse the command line arguments. Makes it a lot easier
    to test CLI parameters.

    This will exit with code 0 and show help if no command is chosen.

    Args
        argv: The command line parameters, minus the name of the script
    Returns
        The parse command line arguments
    """
    parser = ArgumentParser(add_help=False,
                            description=f'mrmat-python-cli-cui - {__version__}')  # NOSONAR
    parser.add_argument('-q', '--quiet', action='store_true', dest='quiet', help='Silent operation')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Debug')
    parser.add_argument('-c', '--config',
                        dest='config',
                        required=False,
                        default=os.path.expanduser(os.path.join('~', '.mrmat-python-cli')))

    command_parser = parser.add_subparsers(dest='command')
    greeting_parser = command_parser.add_parser('greeting',
                                                help='Obtain a greeting',
                                                )
    greeting_parser.add_argument('-n', '--name',
                                 dest='name',
                                 required=False,
                                 help='Name to greet (defaults to "World"')
    greeting_parser.set_defaults(cmd=GreetingCommand)
    ui_demo_parser = command_parser.add_parser('ui-demo',
                                               help='UI Demo')
    ui_demo_parser.set_defaults(cmd=UIDemoCommand)

    long_running_parser = command_parser.add_parser('long-running',
                                                    help='Long Running Command')
    long_running_parser.set_defaults(cmd=LongRunningCommand)

    config_show_parser = command_parser.add_parser('config-show',
                                                   help='Show the current configuration')
    config_show_parser.set_defaults(cmd=ConfigShowCommand)

    args = parser.parse_args(argv)
    if (not hasattr(args, 'command')) or args.command is None:
        parser.print_help()
        return None
    return args


def main(argv=None) -> int:
    """
    Main entry point for the CLI

    Returns
        An exit code. 0 when successful, non-zero otherwise
    """
    args = parse_args(argv if argv is not None else sys.argv[1:])
    if args is None:
        return 0
    config = ConfigParser(strict=True, defaults={'foo': 'bar'})
    if os.path.exists(args.config):
        config.read(args.config)
    else:
        with open(args.config, 'w+', encoding='UTF-8') as c:
            config.write(c)
    cli_ui.setup(verbose=args.debug, quiet=args.quiet, timestamp=False)

    #
    # Execute the command passed in via the parser default
    # Show help if no command was selected

    cmd = args.cmd(args, config)
    return cmd.execute()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
