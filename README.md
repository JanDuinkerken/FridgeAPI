# FridgeAPI

Python3 + MySQL REST API for a fridge contents listing app

## Usage

To run the server install `docker` and `docker-compose` and run the following command on the root directory:

```bash
docker-compose up
```

The app can also be run with python using the method described below (not recommended). 
## Python

To run the development server install the dependencies and simply execute the followng command:

```bash
python3 rest.py
```
### Dependencies

* jsonify
* flask
* flask-ext
* flask-mysql
* pymysql
* typing
* typing_extensions
* datetime
* cryptography

## Endpoints

| **Method** | **Endpoint**           | **Description**                                                              |
|------------|------------------------|------------------------------------------------------------------------------|
| GET        | `/fridges`               | List all fridges                                                             |
| POST       | `/fridges`               | Creates new fridge (Location specified in the request body)                  |
| PUT        | `/fridges/<f_id>`        | Update fridge (Location specified in the request body)                       |
| DELETE     | `/fridges/<f_id>`        | Delete fridge                                                                |
| GET        | `/fridges/<f_id>`        | List items in fridge                                                         |
| POST       | `/fridges/<f_id>`        | Add item (Data specified in the request body)                                |
| PUT        | `/fridges/<f_id>/<i_id>` | Update item with id i_id in fridge f_id (Data specified in the request body) |
| DELETE     | `/fridges/<f_id>/<i_id>` | Delete item with id i_id from fridge with id f_id                            |

