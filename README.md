# SendIT-API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/MissKibetu/SendIT-API.svg?branch=ft-create-order-161827472)](https://travis-ci.org/MissKibetu/SendIT-API)
[![Coverage Status](https://coveralls.io/repos/github/MissKibetu/SendIT-API/badge.svg?branch=ft-cancel-order-161837503)](https://coveralls.io/github/MissKibetu/SendIT-API?branch=ft-cancel-order-161837503)

## The endpoints to be created should enable the user to

* Create a parcel delivery order
* Get all parcel delivery orders
* Get a specific parcel delivery order by ID
* Get a specific parcel delivery order by ID
* Cancel a parcel delivery order

## Functioning endpoints:

| EndPoint                      	| Functionality                    				|  Actual routes                			|
| :---                          	| :---:                        				    |  :---:                      			    |
| POST /create order            	| Create a parcel order            				|  /api/v1/create_order              		|
| GET /all parcel orders        	| Get all available orders         				|  /api/v1/all_orders             			|
| GET /parcel order/<parcelId>   	| Fetch a single order details by parcelId     	|  /api/v1/all_orders/<int:parcelID>     	|
| GET /parcel order/<sender email>  | Fetch a single order details by sender email  |  /api/v1/all_orders/<string:sender_email> |
| PUT /cancel order/<orderId>		| Cancel order (change status to cancelled)    	|  /api/v1/cancel/<int:parcelID>     		|
