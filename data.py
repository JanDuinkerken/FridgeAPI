import pymysql
from db import mysql
import datetime as dt
from typing import TypedDict
from flask import jsonify, request, flash
class Fridge(TypedDict):
    fridge_id: int
    location: str

class Item(TypedDict):
    item_id: int
    fridge_id: int
    i_name: str
    cuantity: int
    drawer: int
    r_date: dt.datetime

def all_fridges():
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * from fridge;")
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def add_fridge():
    try:
        _json = request.json
        _location = _json['location']
        if _location and request.method == 'POST':
            sql = "INSERT INTO fridge (location) VALUES (%s)"
            data = (_location,)
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql, data)
            conn.commit()
            resp = jsonify('Fridge added succesfully!')
            resp.status_code = 200
            return resp
        else:
            not_found()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def update_fridge(id):
    try:
        _json = request.json
        _location =_json['location']
        if _location and request.method == 'PUT':
            sql = "UPDATE fridge SET location = %s WHERE fridgeId = %s"
            data = (_location, id,)
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql, data)
            conn.commit()
            resp = jsonify('Fridge updated succesfully!')
            resp.status_code = 200
            return resp
        else:
            not_found()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def delete_fridge(id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("DELETE FROM fridge WHERE fridgeId = %s", (id,))
        conn.commit()
        resp = jsonify('Fridge deleted succesfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    
def show_items(id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * from item where fridgeId = %s;", (id,))
        rows = cur.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def add_items(id):
    try:
        _json = request.json
        _name = _json['i_name']
        _cuantity = _json['cuantity']
        _drawer = _json['drawer']
        _date = (dt.datetime.today()).strftime('%Y-%m-%d %H:%M:%S')
        if  _name and _cuantity and _date and _drawer and request.method == 'POST':
            sql = "INSERT INTO item (fridgeId, i_name, cuantity, r_date, drawer) VALUES( %s, %s, %s, %s, %s)"
            data = (id, _name, _cuantity, _date, _drawer,)
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql, data)
            conn.commit()
            resp = jsonify('Item added succesfully!')
            resp.status_code = 200
            return resp
        else:
            not_found()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def update_items(f_id, i_id):
    try:
        _json = request.json
        _i_name =_json['i_name']
        _cuantity = _json['cuantity']
        _drawer = _json['drawer']
        if _i_name and _cuantity and _drawer and request.method == 'PUT':
            sql = "UPDATE item SET i_name = %s, cuantity = %s, drawer = %s WHERE fridgeId = %s AND itemId = %s"
            data = (_i_name, _cuantity, _drawer, f_id, i_id,)
            conn = mysql.connect()
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql, data)
            conn.commit()
            resp = jsonify('Item updated succesfully!')
            resp.status_code = 200
            return resp
        else:
            not_found()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def delete_items(f_id, i_id):
    try:
        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("DELETE FROM item WHERE fridgeId = %s and itemId = %s", (f_id,i_id))
        conn.commit()
        resp = jsonify('Item deleted succesfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

def not_found():
    message = {
            'status' : 404,
            'message' : 'Not found: ' + request.url,
        }
    resp = jsonify(message)
    resp.status_code = 404
    return resp