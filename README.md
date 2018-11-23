# SendIT-API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/MissKibetu/SendIT-API.svg?branch=ft-signup-signin-162080580)](https://travis-ci.org/MissKibetu/SendIT-API)
[![Coverage Status](https://coveralls.io/repos/github/MissKibetu/SendIT-API/badge.svg?branch=ch-JWT-Authentication-162170874)](https://coveralls.io/github/MissKibetu/SendIT-API?branch=ch-JWT-Authentication-162170874)

## Database Integration

## Functioning endpoints

| EndPoint                      	| Functionality                    				|  Actual routes                			|
| :---                          	| :---:                        				    |  :---:                      			    |
| POST /User signup     	       	| Registers a user            					|  /api/v2/signup       		      		|
| POST /User signin		           	| Sign in to user account            			|  /api/v2/signin		              		|
| POST /Database Order Creation	    | Create a parcel order            				|  /api/v2/order_request	              	|
| GET /Database Fetch All Orders    | Get all orders         						|  /api/v2/fetch_orders            			|
| GET /Database Fetch Orders by ID  | Fetch a single order details by parcelId     	|  /api/v2/fetch_orders/<int:parcelID>     	|
| GET /Database Fetch Orders by email| Fetch a single order details by sender email |  /api/v2/user_orders_by_email				|
| PUT /Update Destination			| User can update parcel destination	    	|  /api/v2/change_destination    			|
| PUT /Update status and location	| Admin can update parcel status and location   |  /api/v1/cancel/<int:parcelID>     		|
| POST /create order            	| Create a parcel order            				|  /api/v1/create_order              		|
| GET /all parcel orders        	| Get all available orders         				|  /api/v1/all_orders             			|
| GET /parcel order/<parcelId>   	| Fetch a single order details by parcelId     	|  /api/v1/all_orders/<int:parcelID>     	|
| GET /parcel order/<sender email>  | Fetch a single order details by sender email  |  /api/v1/all_orders/<string:sender_email> |
| PUT /cancel order/<orderId>		| Cancel order (change status to cancelled)    	|  /api/v1/cancel/<int:parcelID>     		|


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

##### Link to postman documentation

[Click here to access postman docymentation](https://documenter.getpostman.com/view/5785639/RzZAkJKv)
