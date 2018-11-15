# SendIT-API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/MissKibetu/SendIT-API.svg?branch=ft-create-order-161827472)](https://travis-ci.org/MissKibetu/SendIT-API)
[![Coverage Status](https://coveralls.io/repos/github/MissKibetu/SendIT-API/badge.svg?branch=ch-order-creation-tests-161839122)](https://coveralls.io/github/MissKibetu/SendIT-API?branch=ch-order-creation-tests-161839122)

## The endpoints to be created should enable the user to

* Create a parcel delivery order
* Get all parcel delivery orders
* Get a specific parcel delivery order by ID
* Get a specific parcel delivery order by email
* Cancel a parcel delivery order

## Functioning endpoints

| EndPoint                      	| Functionality                    				|  Actual routes                			|
| :---                          	| :---:                        				    |  :---:                      			    |
| POST /create order            	| Create a parcel order            				|  /api/v1/create_order              		|
| GET /all parcel orders        	| Get all available orders         				|  /api/v1/all_orders             			|
| GET /parcel order/<parcelId>   	| Fetch a single order details by parcelId     	|  /api/v1/all_orders/<int:parcelID>     	|
| GET /parcel order/<sender email>  | Fetch a single order details by sender email  |  /api/v1/all_orders/<string:sender_email> |
| PUT /cancel order/<orderId>		| Cancel order (change status to cancelled)    	|  /api/v1/cancel/<int:parcelID>     		|

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

##### link to Postman Documentation

[Click here for Postman documentation](https://documenter.getpostman.com/view/5785639/RzZAkJKv)
