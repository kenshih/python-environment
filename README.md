# python-environment

I'm trying to figure out a good general py environment setup for all my needs.

At the root is the basic setup.

Progressively, I'm adding more enviroments as need or imagined need arises.

* [Basic](#basic-setup)
* [AWS basic scripting use case](./aws/)
* [Jupyterlab setup](./jupyterlab/)
* [library with setuptools](./library/)
* [rustlib: build rust fn to use in python](./rustlib/)


# Basic setup

- [python-environment](#python-environment)
- [Basic setup](#basic-setup)
  - [pyenv setup](#pyenv-setup)
  - [project setup: virtualenv](#project-setup-virtualenv)

## pyenv setup
1. clean env of python additions/paths etc
2. `brew install pyenv`
3. add pyenv init to .bashrc/.zshrc, respectively
4. install some desired version e.g. `pyenv install 3.10.3`

## project setup: virtualenv

```sh
# in project set local to create `.python-version`
pyenv local 3.10.3
# create a virtual env using python module
python -m venv env
# activate virtual env
source env/bin/activate
# to leave
deactivate
```

ref: [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)