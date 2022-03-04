import pymysql
from app import app
from db import mysql
from data import all_fridges, add_fridge, delete_fridge, delete_items, show_items, add_items, delete_items, update_fridge, update_items, not_found
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

@app.route('/fridges/<int:id>', methods=['DELETE'])
def route_delete_fridge(id):
    return delete_fridge(id)

@app.route('/fridges/<int:id>', methods=['PUT'])
def route_update_fridge(id):
    return update_fridge(id)

@app.route('/fridges/<int:id>')
def route_show_items(id):
    return show_items(id)

@app.route('/fridges/<int:id>', methods=['POST'])
def route_add_items(id):
    return add_items(id)

@app.route('/fridges/<int:f_id>/<int:i_id>', methods=['PUT'])
def route_update_items(f_id, i_id):
    return update_items(f_id, i_id)

@app.route('/fridges/<int:f_id>/<int:i_id>', methods=['DELETE'])
def route_del_items(f_id, i_id):
    return delete_items(f_id, i_id);

@app.errorhandler(404)
def route_not_found(error=None):
    return not_found()

if __name__ == "__main__":
    app.run(host='0.0.0.0')