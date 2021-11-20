# MrMat :: Python CLI

Boilerplate code for a Python CLI

[![Build](https://github.com/MrMatOrg/mrmat-python-cli/actions/workflows/build.yml/badge.svg)](https://github.com/MrMatOrg/mrmat-python-cli/actions/workflows/build.yml)

## Features

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

## How to run this

Install as usual, then execute `mrmat-python-cli -h`.

## Limitations

### Nested Subcommands

It would be desirable to have the ability for nested subcommands such as demonstrated by the Azure CLI
for instance. It is, however, not easily possible to implement such nested commands using the native
argparse without manually modifying argv. An alternative might be [arghandler](https://github.com/druths/arghandler)
but that does not appear to be very maintained.
