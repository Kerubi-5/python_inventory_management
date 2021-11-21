import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('inventory.db')
        return con

    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE inventory(id text PRIMARY KEY not null, name text, description text, unit text, quantity text, Created_at text)")
    con.commit()

def insert_table(items):
    cursorObj = con.cursor()
    cursorObj.execute("INSERT INTO inventory(id, name, description, unit, quantity, Created_at) VALUES(?, ?, ?, ?, ?, ?)", (items))

def update_table(items):
    cursorObj = con.cursor()
    sql = ("UPDATE inventory SET name = ?, description = ?, unit = ?, quantity = ?, Created_at = ? WHERE id = ?")
    cursorObj.execute(sql, items)

#SELECTION FOR UPDATE OPERATION
def selectkey_table_upd(id_no, items):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT id from inventory")
    rows = cursorObj.fetchall()

    for row in rows:
        if row[0] == id_no:
            update_table(items)

def del_table(row):
    cursorObj = con.cursor()
    sql = "DELETE from inventory where id = ?"
    cursorObj.execute(sql, (row[0], ))

#SELECTION FOR DELETE OPERATION
def selectkey_table_del(id_no):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT id from inventory")
    rows = cursorObj.fetchall()

    for row in rows:
        if row[0] == id_no:
            del_table(row)

def save_table():
    con.commit()

def get_table():
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * from inventory ORDER BY id")

    return cursorObj.fetchall()

con = sql_connection()

#sql_table(con)
# id_num = input("Input ID NO: ")
# item_name = input("Input item name: ")
# item_desc = input("Input item description: ")
# item_unit = input("Input item unit: ")
# item_qty = int(input("Input item quantity: "))
# item_date = input("Input when the item was created: ")
# items = (id_num, item_name, item_desc, item_unit, item_qty, item_date)