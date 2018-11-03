# store-api-v2
[![Build Status](https://travis-ci.com/jomasim/store-api-v2.svg?branch=dev)](https://travis-ci.com/jomasim/store-api-v2)
[![Coverage Status](https://coveralls.io/repos/github/jomasim/store-api-v2/badge.svg?branch=dev)](https://coveralls.io/github/jomasim/store-api-v2?branch=dev)
[![Maintainability](https://api.codeclimate.com/v1/badges/2454765c63bab49e3fb1/maintainability)](https://codeclimate.com/github/jomasim/store-api-v2/maintainability)


store-api-v2 is a restful api to power  storeManager app front-end pages.
It uses postgres database and jwt authentication for all its endpoints.

# Requirements
- python3 - [Python](https://www.python.org/)
- pip - [Install pip](https://pip.pypa.io/en/stable/installing/)
- virtualenv - [install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

# Endpoints
| Http Method | Route | Functionality |
| ----------- | ----- | ------------- |
| POST        | /api/v2/login | user login|
| DELETE      | /api/v2/logout| revoking user token|
| POST        | /api/v2/user | create user|
| POST        | /api/v2/products| create product |
| PUT         | /api/v2/products/productId| update product |
| GET      	  | /api/v2/products/productId| get product by id |
| GET      	  | /api/v2/products/ | get all products|
| POST        | /api/v2/sales/ | create sale|
| GET         | /api/v2/sales/ | get all sales |
| GET         | /api/v2/sales/sale_id | get sale by id|


# Setup 

clone repo from github

```
$ git clone https://github.com/jomasim/store-api-v2.git 
$ cd store-api-v2 
$ git checkout dev

```

Create a virtual environment

```
$ python3 -m venv venv

```

Activate the virtual environment

```
$ . venv/bin/activate

```

Install project dependencies

```
$ pip install -r requirements.txt

```

setup  the .env file.

```
$ cp .env.example .env

```

	production/stagiging database

		`DBHOST` - The production/staging database host.

		`DBUSER` - The production/staging database user.

		`DBNAME` - The production/staging database name.

		`DBPASS` - The production/staging database password.

	testing db config(used when running tests)

		`TEST_DBHOST` - The testing database host.

		`TEST_DBUSER` - The testing database user.

		`TEST_DBNAME` - The testing database name.

		`TEST_DBPASS` - The testing database password.


	setup jwt 

		JWT_SECCRET=`$SECRET_KEY$` - A random key that is used by the 
		application to generate secure authentication tokens(jwt)

		JWT_BLACKLIST=True  - Enables revoking of tokens when the user logs out


Running app

```
$ python3 run.py 

```

# Running tests
```
$ pytest tests -v

```

# Documentation

Find store-api-v2 docs [here](https://storeapiv2.docs.apiary.io/)

# Framework 
Python Flask 

