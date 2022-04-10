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
Main entry point for the Python CLI implementation
"""

import sys
import typing
import argparse
from configparser import ConfigParser
import inspect

from mrmat_python_cli import __version__
from mrmat_python_cli.commands import (
    GreetingCommand,
    UIDemoCommand,
    LongRunningCommand,
    ResourceCommands)


def inline_cmd(args: argparse.Namespace, config: ConfigParser) -> int:  # pylint: disable=W0613
    print('I am an inline command')
    return 0


def main(args: typing.List) -> int:
    """
    Main entry point for the CLI

    Returns
        An exit code. 0 when successful, non-zero otherwise
    """
    parser = argparse.ArgumentParser(add_help=False, description=f'{__name__} - {__version__}')
    parser.add_argument('-q', '--quiet', action='store_true', dest='quiet', help='Silent operation')
    parser.add_argument('-d', '--debug', action='store_true', dest='debug', help='Debug')
    parser.add_argument('-c', '--config', dest='config', help='Configuration file')
    subparsers = parser.add_subparsers(dest='group')

    greeting_parser = subparsers.add_parser(name='greeting', help='Obtain a greeting')
    greeting_parser.add_argument('--name', '-n',
                                 dest='name',
                                 type=str,
                                 required=False,
                                 default='World',
                                 help='The name to greet')
    greeting_parser.set_defaults(cmd=GreetingCommand)

    ui_demo_parser = subparsers.add_parser(name='ui', help='Show a UI demo')
    ui_demo_parser.set_defaults(cmd=UIDemoCommand)

    long_cmd_parser = subparsers.add_parser(name='long', help='Execute a long running command')
    long_cmd_parser.set_defaults(cmd=LongRunningCommand)

    inline_cmd_parser = subparsers.add_parser(name='inline', help='Execute an inline command')
    inline_cmd_parser.set_defaults(cmd=inline_cmd)

    resource_parser = subparsers.add_parser(name='resource', help='Resource commands')
    resource_subparser = resource_parser.add_subparsers()
    resource_list_parser = resource_subparser.add_parser(name='list', help='List all resources')
    resource_list_parser.set_defaults(cmd=ResourceCommands.list)
    resource_get_parser = resource_subparser.add_parser(name='get', help='Get a resource')
    resource_get_parser.add_argument('--id',
                                     dest='id',
                                     type=int,
                                     required=True,
                                     help='The resource id to get')
    resource_get_parser.set_defaults(cmd=ResourceCommands.get)
    resource_create_parser = resource_subparser.add_parser(name='create', help='Create a resource')
    resource_create_parser.set_defaults(cmd=ResourceCommands.create)
    resource_modify_parser = resource_subparser.add_parser(name='modify', help='Modify a resource')
    resource_modify_parser.add_argument('--id',
                                        dest='id',
                                        type=int,
                                        required=True,
                                        help='The resource id to modify')
    resource_modify_parser.set_defaults(cmd=ResourceCommands.modify)
    resource_remove_parser = resource_subparser.add_parser(name='remove', help='Remove a resource')
    resource_remove_parser.add_argument('--id',
                                        dest='id',
                                        type=int,
                                        required=True,
                                        help='The resource id to remove')
    resource_remove_parser.set_defaults(cmd=ResourceCommands.remove)

    args = parser.parse_args(args)

    config = ConfigParser(strict=True, defaults=dict(foo='bar'))
    if args.config:
        config.read(args.config)

    if hasattr(args, 'cmd'):
        # This may be simplified to just args.cmd(args, config) if you don't use command classes
        return args.cmd(args, config)() if inspect.isclass(args.cmd) else args.cmd(args, config)
    elif hasattr(args, 'group'):
        subparser = subparsers.choices.get(args.group)
        subparser.print_help() if subparser else parser.print_help()    # pylint: disable=W0106
    else:
        parser.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
