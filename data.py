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
