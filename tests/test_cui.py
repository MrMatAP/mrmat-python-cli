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

from mrmat_python_cli.cui import main


def test_toplevel_help(capsys):
    ret = main([])
    captured = capsys.readouterr()
    assert ret == 1
    assert '{greeting,ui,long,inline,resource}' in captured.out


def test_inline(capsys):
    ret = main(['inline'])
    captured = capsys.readouterr()
    assert ret == 0
    assert 'I am an inline command' in captured.out


def test_greeting(capsys):
    ret = main(['greeting', '--name', 'Eelyn'])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == 'Hello Eelyn\n'


def test_long(capsys):
    ret = main(['long'])
    #captured = capsys.readouterr()
    assert ret == 0
    # TODO: cli_ui output doesn't seem to be captured
    #assert 'I\'m going to take a while' in captured.out
    #assert 'Done' in captured.out


def test_ui(capsys):
    ret = main(['ui'])
    #captured = capsys.readouterr()
    assert ret == 0
    # TODO: cli_ui output doesn't seem to be captured
    #assert 'Labelled Progress' in captured.out
    #assert 'This is a warning message' in captured.err


def test_resource(capsys):
    ret = main(['resource'])
    captured = capsys.readouterr()
    assert ret == 1
    assert '{list,get,create,modify,remove}' in captured.out


def test_resource_list(capsys):
    ret = main(['resource', 'list'])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == 'I would return a list of resources\n'


def test_resource_get(capsys):
    ret = main(['resource', 'get', '--id', '1'])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == 'I would return resource with id 1\n'


def test_resource_create(capsys):
    ret = main(['resource', 'create'])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == 'I would create a resource\n'


def test_resource_modify(capsys):
    ret = main(['resource', 'modify', '--id', '1'])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == 'I would modify a resource with id 1\n'


def test_resource_remove(capsys):
    ret = main(['resource', 'remove', '--id', '1'])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == 'I would remove a resource with id 1\n'
