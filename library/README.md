# library

basic lib setup that can be packaged and distributed

# how to use

```
# get into venv
source env/bin/activate

# load requirements for build management
python -m pip install -r build.requirements.txt

# you build a distribution like this, which creates wheel & zip file in dist
python -m build
```

Example of using the library in a new env
```
cd test-env
python -m venv env\n# activate virtual env\nsource env/bin/activate
python -m pip install ../library/dist/mypackage-0.0.1-py3-none-any.whl
python -m mypackage
> Hello world. Defined in init
> but called from __main__
```

# original setup

same setup as [parent](../README.md)

then...

```
python -m venv env
# activate virtual env
source env/bin/activate

# install packages
python -m pip install --upgrade setuptools
> Successfully installed setuptools-62.0.0

# config following: https://setuptools.pypa.io/en/latest/userguide/quickstart.html
# `pyproject.toml`
# `setup.cfg`
# `mypackage/__init__.py`
python -m pip install build

# freeze into requirements
python -m pip freeze > build.requirements.txt

# then, later on you can load them like this
python -m pip install -r build.requirements.txt
```
