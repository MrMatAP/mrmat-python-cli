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

