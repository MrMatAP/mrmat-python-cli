# MrMat :: Python CLI

Boilerplate code for a Python CLI

[![Build](https://github.com/MrMatAP/mrmat-python-cli/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-cli/actions/workflows/build.yml)

## How to use this

Install as usual, then execute `mrmat-python-cli -h`, featuring

* A command delegation method
* Long running commands
* Reasonably nice output

## How to build this

Building a wheel boils down to this:

```shell
$ pip install -r requirements.txt
$ PYTHONPATH=$(pwd) python -m build --wheel
```

This project uses the [PEP517 build mechanism](https://www.python.org/dev/peps/pep-0517/), but with a twist so CI is in
control over the generation of the micro version number. In our case, CI is GitHub Actions, which has the top-level
environment variables `MAJOR` and `MINOR`. These two are intended to be infrequently updated manually if and when
it is needed. The micro version is automatically set by the `GITHUB_RUN_NUMBER` which increases for every build
we do. The `MRMAT_VERSION` environment variable is a concatenation of these three. If the build is via a PR onto
main then this is the release version. Otherwise `.dev0` is appended to the version.

If you are building locally, then your version will **always** be `0.0.0.dev0` (unless you explicitly set the
`MRMAT_VERSION` environment variable to something different). 

It is necessary for setup.cfg to figure out whether and what `MRMAT_VERSION` is set to. Since this is no longer
an executable in PEP517, we tell it to use the `ci` module for doing so. The `ci` module simply picks up `MRMAT_VERSION`
from the environment, no more and the module is explicitly ignored from packaging. However, you must ensure that
the top-level `ci` module is on the Python path as you build (hence the setup above).

## How this works

We want the flexibility of calling 

* a traditional garden-variety command with parameters, e.g. (mrmat-python-cli --param)
* a subcommand thereof, e.g. (mrmat-python-cli greeting --name)
* and sub-subcommands/command groups thereof, e.g. (mrmat-python-cli resource get --id 1)

The first two are easily modeled using argparse. The third is a bit less obvious but becomes easy to implement
when you know that you can call `add_subparsers(dest='group')`. This makes the command group visible after parsing.

The execution of the commands still works best by assigning them a callable via `set_defaults(cmd=CALLABLE)` that you
then execute via `args.cmd()`. You will frequently find that this callable should adhere to some standards, for instance
you want to pass the parsed arguments and app configuration to it, e.g. `args.cmd(args, config)`. If your app is 
reasonably small and you have the discipline then you can just pay attention yourself as we demonstrate with the
`inline` command. As your app grows, you may wish to enforce this a bit by using an abstract base class enforcing that
standard. If then your app is also no longer stateless, using command classes also opens the door to the command pattern
where you might implement an undo/rollback or other patterns. For a typical small CLI app that is stateless doing so
is total overkill though and you'll find a comment in the sample code how the invocation of that command can be
simplified if you don't need it.

You will need to recognize whether a sub-command/command group was invoked without the required sub-subcommand. In order
to do this you can simply check whether `group` is present but not `cmd` and then force help on the subparser to be
shown.
