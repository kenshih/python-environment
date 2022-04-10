# rustlib

# how to use

see: https://github.com/PyO3/pyo3
this just follows that

```
# get into venv
source env/bin/activate
python -m pip install -r build.requirements.txt
# try local development
maturin develop
python
>>> import rustlib
>>> rustlib.sum_as_string(5, 20)
maturin build

# try installing and importing it in a new env
cd ../test-env
source env/bin/activate
python -m pip install ../rustlib/target/wheels/rustlib-0.1.0-cp310-cp310-macosx_10_7_x86_64.whl
python
>>> import rustlib
>>> rustlib.sum_as_string(5, 55)
'60'
```


# original setup

same setup as [parent](../README.md)

then...

```
python -m venv env
# activate virtual env
source env/bin/activate
python -m pip install -r build.requirements.txt

# https://github.com/PyO3/pyo3
python -m pip install maturin
maturin init
# use pyo3
# ^ generated: `Cargo.toml` `pyproject.toml` `.gitignore` `.github/workflows`
maturin develop
python
>>> import rustlib
>>> rustlib.sum_as_string(5, 20)
'25'

# freeze into requirements
python -m pip freeze > build.requirements.txt
# then manually removed the `rustlib` dep

# then, later on you can load them like this
python -m pip install -r build.requirements.txt

................

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
