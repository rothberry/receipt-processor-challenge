# Setup for python and Pipenv

Make sure you have python3 and pip installed.

The repo will be running python 3.8.13

Commands to run:

```shell
pip install pipenv

pipenv install
# this will install all dependencies from the Pipfile.lock

# =====
# OPTION 1

# To run the Flask server defaulted to port 5000
pipenv run flask run

# To run the pytest suite
pipenv run pytest -v
# -v adds more useful verbose output
# =====

# =====
# OPTION 2
pipenv shell
# opens the virtual environment so you don't need to start with `pipenv run`

flask run 

pytest -v
# =====

```

# Docker setup

```shell
docker pull rothberry/receipt_flask
```
