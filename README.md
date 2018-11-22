# SendIT-API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/MissKibetu/SendIT-API.svg?branch=ft-signup-signin-162080580)](https://travis-ci.org/MissKibetu/SendIT-API)
[![Coverage Status](https://coveralls.io/repos/github/MissKibetu/SendIT-API/badge.svg?branch=ft-update-orders-162159818)](https://coveralls.io/github/MissKibetu/SendIT-API?branch=ft-update-orders-162159818)

## Database Integration

## The endpoints to be created should eneble

* The user can create user accounts and can sign in to the app.
* The user can change the destination of a parcel delivery order.
* The user can view all parcel delivery orders he/she has created.
* Admin can view all parcel delivery orders in the application.
* Admin can change the status of a parcel delivery order.
* Admin can change the present location of a parcel delivery order 

## Database to be used

 ```PostgreSQL```
 
## Other requirements

* implementation of token-based authentication using JSON web token (JWT) and the security of all routes using JSON web token.

## Technology used

* Python 3.7
* Flask framework
* Unittest for testing

## Testing the endpoints

>To run and test SendIT-API, you will need to install python 3.6, Flask and Postman

##### Clone the repository to your local environment

```
$ git clone https://github.com/MissKibetu/SendIT-API.git
$ cd SendIT-API
```

##### Create the virtualenv and activate it

```
$ virtualenv venv
$ cd SendIT-API/venv/Scripts
$ activate
```

##### Install dependencies in root folder

```
$ pip install -r requirements.txt
```

##### Run the app from the root folder

```
$ python run.py
```

##### Command to run tests from the root folder

```
coverage run --source=api -m pytest && coverage report
```
