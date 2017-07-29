Python Project Boilerplate
==========================

This repo provides a standardized template for modern Python projects based
on the layout [recommended by Kenneth Reitz](http://www.kennethreitz.org/essays/repository-structure-and-python).

This version adds:
* Support for installing development dependencies through setup.py
* PyTest unit-test support
* An [.editorconfig](http://editorconfig.org/) file
* Sphinx documentation generation through setup.py

## Getting Started

The project is ready to run as is. You will need Python 2.7 or later.

### Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv .virtualenv
```

if the `pyvenv` command does not exist on your system.

### Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source .virtualenv/bin/activate
```

On Windows:

```
.virtualenv\Scripts\activate.bat
```

### Install the Development Environment

Now run:

```
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

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
python setup.py doc
```

The generated documentation will be available in `docs/_build`

