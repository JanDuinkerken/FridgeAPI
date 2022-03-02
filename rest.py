import pymysql
from app import app
from db import mysql
from data import all_fridges, add_fridge, delete_fridge
from flask import jsonify
from flask import flash, request

@app.route('/')
def route_hello_world():
    return "Hello, World!"

@app.route('/fridges')
def route_all_fridges():
    return all_fridges()

@app.route('/fridges', methods=['POST'])
def route_add_fridge():
    return add_fridge()

@app.route('/delete/fridge/<int:id>', methods=['DELETE'])
def route_delete_fridge(id):
    return delete_fridge(id)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'Not found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run()