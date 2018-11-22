# SendIT-API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/MissKibetu/SendIT-API.svg?branch=ft-signup-signin-162080580)](https://travis-ci.org/MissKibetu/SendIT-API)
[![Coverage Status](https://coveralls.io/repos/github/MissKibetu/SendIT-API/badge.svg?branch=ft-view-orders-162159675)](https://coveralls.io/github/MissKibetu/SendIT-API?branch=ft-view-orders-162159675)

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

## Functioning endpoints

| EndPoint                      	| Functionality                    				|  Actual routes                	|
| :---                          	| :---:                        				    |  :---:                      	    |
| POST /User Signup                	| Users can create accounts            			|  /api/v2/signup              		|
| POST /User Signin                	| Users can log in to accounts            		|  /api/v2/signin              		|
