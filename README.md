Python Project Boilerplate
==========================

This repo provides a standardized template for modern Python projects based
on the layout [recommended by Kenneth Reitz](http://www.kennethreitz.org/essays/repository-structure-and-python).

Features:
* Editable install support
* Support for installing development dependencies through setup.py
* PyTest unit-test support
* PyLint
* An [.editorconfig](http://editorconfig.org/) file
* Sphinx documentation generation
* `pyproject.toml` PEP 517/518 support

# Getting Started

The project is ready to run as is. You will need Python 2.7 or later.

## Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv .virtualenv
```

if the `pyvenv` command does not exist on your system.

## Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source .virtualenv/bin/activate
```

On Windows:

```
.virtualenv\Scripts\activate.bat
```

## Install the Development Environment

Now run:

```
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

* The `-e` option specifies that you wish to install the package in "editable" mode for development.
* The `.[dev]` argument directs pip to install the package that is defined by the `setup.py` file the in the current directory and to additionally install the extra depdencies defined in the "dev" group. The additional dependencies include things lik ethe Sphinx documentation generator, pytest, pylint and other development packages that end-users of the package will not need.

Refer to the [pip install documentation](https://pip.pypa.io/en/stable/reference/pip_install/#) for more information on these options.

At this point, you are ready to start modifying to template for your own needs.

## Testing

You can run unit tests through setup.py with:

```
python setup.py test
```

or just run pytest directly:

```
pytest
```

## Documentation

To generate Sphinx documentation, run:

```
python setup.py build_sphinx
```

The generated documentation will be available in `build/sphinx`

## Distribution

When you are ready to distribute your Python package, build a wheel with:

```
python setup.py bdist_wheel
```

> Alternatively, you can add the `--universal` option to the `bdist_wheel` command to build a "univeral" distribution that can be used with both Python 3.x and 2.7.x.

The wheel will be generated in th `dist` directory.
