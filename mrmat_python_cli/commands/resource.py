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
Implementation of resource commands
"""

import argparse
from configparser import ConfigParser

from mrmat_python_cli.commands import AbstractResourceCommands


class ResourceCommands(AbstractResourceCommands):
    """
    Implementation of resource commands
    """

    @staticmethod
    def list(args: argparse.Namespace, config: ConfigParser) -> int:
        print('I would return a list of resources')
        return 0

    @staticmethod
    def get(args: argparse.Namespace, config: ConfigParser) -> int:
        print(f'I would return resource with id {args.id}')
        return 0

    @staticmethod
    def create(args: argparse.Namespace, config: ConfigParser) -> int:
        print('I would create a resource')
        return 0

    @staticmethod
    def modify(args: argparse.Namespace, config: ConfigParser) -> int:
        print(f'I would modify a resource with id {args.id}')
        return 0

    @staticmethod
    def remove(args: argparse.Namespace, config: ConfigParser) -> int:
        print(f'I would remove a resource with id {args.id}')
        return 0
