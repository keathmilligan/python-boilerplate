Python Project Boilerplate
==========================

This repo provides a standardized template for Python package projects. The project structure is based on the layout [recommended by Kenneth Reitz](https://kennethreitz.org/essays/2013/01/27/repository-structure-and-python) with a few modern updates.

> This template is best suited for projects such as a library or framework that you intend to publish to a public or private repository. For general applications, I recommend the [Python Application Template](https://github.com/keathmilligan/python-app-template) instead. For web applications and services, see [Flask Quick Start](https://github.com/keathmilligan/flask-quickstart) and [Flask Service](https://github.com/keathmilligan/flask-service).

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
python -m venv myvirtualenv
```

for Python 3.x.

For Python 2.7, use the `virtualenv` command:

```
virtualenv myvirtualenv
```

This will create the virtual environment in the current directory as `myvirtualeenv`. You can place the virtual environment in any location. Alternative, you can use any of a number of tools for managing Python virtual environments. See note below on `pipenv`, a popular option.

## Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source myvirtualeenv/bin/activate
```

On Windows with `cmd.exe`:

```
myvirtualeenv\Scripts\activate.bat
```

Or Windows with PowerShell:

```
.\myvirtualeenv\Scripts\activate.ps1
```

## Install the Development Environment

Now run:

```
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

* The `-e` option specifies that you wish to install the package in "editable" mode for development.
* The `.[dev]` argument directs pip to install the package that is defined by the `setup.py` file the in the current directory and to additionally install the extra dependencies defined in the "dev" group. The additional dependencies include things like the Sphinx documentation generator, pytest, pylint and other development packages that end-users of the package will not need.

Refer to the [pip install documentation](https://pip.pypa.io/en/stable/reference/pip_install/#) for more information on these options.

At this point, you are ready to start modifying to template for your own needs.

## (Optional) Using Pipenv

If you prefer to use [pipenv](https://pipenv.pypa.io/en/latest/) to manage your virtual environments, you can run:

```
pipenv install -e .[dev]
```

This will have the same effect as above except that everything will be installed into a virtual environment created by 
pipenv.

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

> Alternatively, you can add the `--universal` option to the `bdist_wheel` command to build a "universal" distribution that can be used with both Python 3.x and 2.7.x.

The wheel will be generated in the `dist` directory.
