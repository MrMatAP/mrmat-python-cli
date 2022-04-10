# MrMat :: Python CLI

Boilerplate code for a Python CLI

[![Build](https://github.com/MrMatOrg/mrmat-python-cli/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-cli/actions/workflows/build.yml)

## Features

* A command delegation method
* Long running commands
* Nice output

## How to build this

Use the standard `python ./setup.py install` to build. By default, the version built will be `0.0.0.dev0`,
unless the `MRMAT_VERSION` environment variable is set by the build orchestrator (e.g. GitHub Actions). The
version and whether a release is built is consequently controlled exlusively by the build orchestrator.

## How to run this

Install as usual, then execute `mrmat-python-cli -h`.

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
