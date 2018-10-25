# store-api-v2
[![Build Status](https://travis-ci.com/jomasim/store-api-v2.svg?branch=dev)](https://travis-ci.com/jomasim/store-api-v2)
[![Coverage Status](https://coveralls.io/repos/github/jomasim/store-api-v2/badge.svg?branch=dev)](https://coveralls.io/github/jomasim/store-api-v2?branch=dev)
[![Maintainability](https://api.codeclimate.com/v1/badges/2454765c63bab49e3fb1/maintainability)](https://codeclimate.com/github/jomasim/store-api-v2/maintainability)


store-api-v2 is a restful api to enable admin manage storeManager app
it uses postgres database and jwt authentication for all endpoints

# Requirements
- `python3` - [Python](https://www.python.org/)
- `pip` - [Install pip](https://pip.pypa.io/en/stable/installing/)
- `virtualenv` - [install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

# Endpoints
| Http Method | Route | Functionality |
| ----------- | ----- | ------------- |
| POST        | /api/v2/auth | user login|
| POST        | /api/v2/user | create user|
| POST        | /api/v2/products| create product |
| PUT         | /api/v2/products/productId| update product |
| DELETE      | /api/v2/products/productId| delete product |


# Setup 

clone repo from github

- `$ git clone https://github.com/jomasim/store-api-v1.git`
- `$ cd store-api-v1`
- `$ git checkout dev `

Create a virtual environment

`$ python3 -m venv venv`

Activate the virtual environment

`$ . venv/bin/activate`

Install project dependencies

`$ pip install -r requirements.txt`

setup  the .env file.

`$ cp .env.example .env`

production/stagiging database

`DB_HOST` - The production/staging database host.

`DB_USER` - The production/staging database user.

`DB_NAME` - The production/staging database name.

`DB_PASS` - The production/staging database password.

testing db config(used when running tests)

`TEST_DBHOST` - The testing database host.

`TEST_DBUSER` - The testing database user.

`TEST_DBNAME` - The testing database name.

`TEST_DBPASS` - The testing database password.


set jwt secret

`JWT_SECCRET=$SECRET_KEY$` - A random key that is used by the application to generate secure        authentication tokens(jwt).


Running app

`$ python3 run.py `

# Running tests
`$ pytest tests`

# Documentation


# Framework 
Python Flask 

