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

## Limitations

### Nested Subcommands

It would be desirable to have the ability for nested subcommands such as demonstrated by the Azure CLI
for instance. It is, however, not easily possible to implement such nested commands using the native
argparse without manually modifying argv. An alternative might be [arghandler](https://github.com/druths/arghandler)
but that does not appear to be very maintained.