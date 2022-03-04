# FridgeAPI

Python3 + MySQL REST API for a fridge contents listing app

## Python dependencies (install with pip3)

* jsonify
* flask
* flask-ext
* flask-mysql
* pymysql
* typing
* datetime
* cryptography

To run the development server simply execute the followng command:

```bash
python3 rest.py
```

## Endpoints

| **Method** | **Endpoint**           | **Description**                                                              |
|------------|------------------------|------------------------------------------------------------------------------|
| GET        | /fridges               | List all fridges                                                             |
| POST       | /fridges               | Creates new fridge (Location specified in the request body)                  |
| PUT        | /fridges/<f_id>        | Update fridge (Location specified in the request body)                       |
| DELETE     | /fridges/<f_id>        | Delete fridge                                                                |
| GET        | /fridges/<f_id>        | List items in fridge                                                         |
| POST       | /fridges/<f_id>        | Add item (Data specified in the request body)                                |
| PUT        | /fridges/<f_id>/<i_id> | Update item with id i_id in fridge f_id (Data specified in the request body) |
| DELETE     | /fridges/<f_id>/<i_id> | Delete item with id i_id from fridge with id f_id                            |

## TODO

* Deploy on docker
