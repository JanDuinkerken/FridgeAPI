import pymysql
from db import mysql
import datetime as dt
from typing import TypedDict
from flask import jsonify, request, flash
class Fridge(TypedDict):
    fridge_id: int
    location: str
    n_items: int

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
            sql = "INSERT INTO fridge (location, n_items) VALUES( %s, 0)"
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