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
Implementation of the UIDemo Command
"""

import time

from rich import box
from rich.progress import Progress, track
from rich.table import Table
from rich.tree import Tree

from mrmat_python_cli import console, log
from mrmat_python_cli.commands import AbstractCommand


class UIDemoCommand(AbstractCommand):
    """
    Implementation of the UIDemo Command
    """

    def __call__(self) -> int:
        console.rule('[bold] Messages')
        log.info('This is an info message')
        log.warning('This is a warning message (on stderr)')
        log.error('This is an error message (on stderr)')
        # log.fatal('This is a fatal message (on stderr, exits)')
        log.debug('This is a debug message')
        try:
            _ = 7 / 0
        except ZeroDivisionError:
            log.exception("You're doing something silly")

        console.rule('[bold] Formatting')
        console.print('This is [bold blue on white]bold blue on white[/]. This is [bold]bold[/bold]. '
                      'Visit this [link=https://www.google.com]link[/link]! '
                      'Emojis are also possible: :red_heart:')

        console.rule('[bold] Tables')
        table = Table(title='Table Demo', box=box.SIMPLE_HEAVY)
        table.add_column('foo')
        table.add_column('bar')
        table.add_column('baz')
        table.add_row('1', '2', '3')
        table.add_row('fee', 'fie', 'foe')
        table.add_row('uno', 'dos', 'tres')
        console.print(table)

        console.rule('[bold] Trees')
        tree = Tree('Tree Demo')
        foo_tree = Tree('foo')
        _ = [foo_tree.add(e) for e in ['1', '2', '3']]
        tree.add(foo_tree)
        tree.add('bar').add('fee').add('fie').add('fum')
        tree.add('baz')
        console.print(tree)

        console.rule('[bold] Labelled Progress')
        try:
            with Progress() as progress:
                task1 = progress.add_task('[red]Downloading...', total=100)
                task2 = progress.add_task('[green]Processing...', total=100)
                task3 = progress.add_task('[cyan]Cooking...', total=100)
                while not progress.finished:
                    progress.update(task1, advance=0.5)
                    progress.update(task2, advance=0.3)
                    progress.update(task3, advance=0.9)
                    time.sleep(0.02)
        except KeyboardInterrupt:
            log.info('Cancelled job')

        console.rule('[bold] Tracking progress')
        try:
            for _ in track(range(30), description='Processing...'):
                time.sleep(0.2)
        except KeyboardInterrupt:
            log.info('Cancelled job')

        return 0
