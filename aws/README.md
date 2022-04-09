# aws example

- [aws example](#aws-example)
- [how to run](#how-to-run)
- [original setup](#original-setup)
  - [setup](#setup)
  - [app creation](#app-creation)

# how to run
```
source env/bin/activate
export AWS_PROFILE=prod
python bin/main.py --envfile "resources/dev2.toml"
```

# original setup

same setup as [parent](../README.md)

then...

## setup
```
python -m venv env
# activate virtual env
source env/bin/activate

# install deps you want
aws python -m pip install "boto3[crt]"
# to revert:
#pip uninstall awscrt
#python -m pip install boto3
python -m pip install toml

# freeze into requirements
python3 -m pip freeze > requirements.txt

# then, later on you can load them like this
python3 -m pip install -r requirements.txt
```

## app creation

