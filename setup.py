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

import os
from setuptools import setup

setup(
    name='mrmat-python-cli',
    version=os.environ['MRMAT_VERSION'] if 'MRMAT_VERSION' in os.environ else '0.0.0.dev0',
    packages=['mrmat_python_cli', 'mrmat_python_cli.commands'],
    license='MIT',
    author='Mathieu Imfeld',
    author_email='imfeldma+9jqerw@gmail.com',
    description='Boilerplate for a Python CLI',

    setup_requires=['flake8'],

    entry_points={
        'console_scripts': [
            'mrmat-python-cli = mrmat_python_cli.cui:main'
        ]
    }
)
