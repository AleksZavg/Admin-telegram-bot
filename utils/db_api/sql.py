import sqlite3
from data.config import data as sdata

''' 
data = {"username": "",
        "telegram_id": "", # int 
        "phone": "",
        "data_add": ""}
'''

# Эти функции админа, и только!
async def check(data):
    db = sqlite3.connect("./main.db")
    sql = db.cursor()
    sql.execute('SELECT telegram_id FROM white_list WHERE telegram_id=?', (data["telegram_id"],))
    if sdata["main_admin_id"] == data["telegram_id"]:
        return "This is admin"
    if sql.fetchone() is None:
        return "not in base"
    else:
        return "is in base"


async def write(data):
    res = await check(data)
    if res == "is in base":
        return "User is in the base"
    elif res == "not in base":
        db = sqlite3.connect("./main.db")
        sql = db.cursor()
        sql.execute("INSERT INTO white_list VALUES (?, ?, ?, ?)", (data["username"], data["telegram_id"], data["phone"], data["data_add"]))
        db.commit()
        return "Succeed write"

async def delete(data):
    if data["telegram_id"] == sdata["main_admin_id"]:
        return "You can not delete admin"
    elif data["telegram_id"] != sdata["main_admin_id"]:
        res = await check(data)
        if res == "not in base":
            return "User is not in the base"
        elif res == "is in base":
            db = sqlite3.connect("./main.db")
            sql = db.cursor()
            sql.execute('DELETE FROM white_list WHERE telegram_id=?', (data["telegram_id"],))
            db.commit()
            return "Succeed delete"

async def all_from_base():
    db = sqlite3.connect("./main.db")
    sql = db.cursor()
    sql.execute('SELECT * FROM white_list')
    return sql.fetchall()

async def all_info(data):
    res = await check(data)
    if res == "not in base":
        return "User is not in the base"
    elif res == "is in base":
        db = sqlite3.connect("./main.db")
        sql = db.cursor()
        sql.execute('SELECT * FROM white_list WHERE telegram_id=?', (data["telegram_id"],))
        return sql.fetchone()

