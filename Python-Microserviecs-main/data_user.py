import sqlite3
import os

#File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "db_user.db")

def user_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price ,instock
        FROM items 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock' : row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_username(user):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price ,instock
        FROM items 
        WHERE name=?
    """
    val = (user,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'name': row[0],
        'category': row[1],
        'price': row[2],
        'instock' : row[3]
        }
    data.append(record)
    
    conn.close()
    return data

def user_name_add(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO items(name,category,price,instock)
        VALUES(?,?,?,?)
    """
    val = (name,category,price,instock)
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Created successfully"

def update_item(name ,category, price, instock, prename):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE items
        SET name=? ,category=? ,price=? ,instock=?
        WHERE name=?
    """
    val = (name, category ,price, instock ,prename)
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Update successfully"

def delete_user(user):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM items
        WHERE name = ?
    """
    conn.execute(sql, (user,))
    conn.commit()
    conn.close()
    return "Deleted successfully"