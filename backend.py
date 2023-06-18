
import sqlite3


def connect():
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY , p_name text, p_price text, p_man text, p_exp text, p_comp text)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY , e_name text, e_age text, e_salary text)")
    conn.commit()
    conn.close()


def insert_product(p_name, p_price, p_man, p_exp, p_comp):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO products VALUES (NULL,?,?,?,?,?)", (p_name, p_price, p_man, p_exp, p_comp))
    conn.commit()
    conn.close()


def view_product():
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_product(p_name="",p_price="", p_man="", p_exp="", p_comp=""):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products where p_name=? OR p_price=? OR p_man=? OR p_exp=? or p_comp=?", (p_name, p_price, p_man, p_exp, p_comp))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_product(id):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM products where id=?", (id,))
    conn.commit()
    conn.close()


def update_product(id, p_name, p_price, p_man, p_exp, p_comp):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("UPDATE products set p_name=?, p_price=?, p_man=?, p_exp=?, p_comp=? WHERE id=?", (p_name, p_price, p_man, p_exp, p_comp, id))
    conn.commit()
    conn.close()


def insert_employee(e_name, e_age, e_salary):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO employee VALUES (NULL,?,?,?)", (e_name, e_age, e_salary))
    conn.commit()
    conn.close()


def view_employee():
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_employee(e_name="", e_age="", e_salary=""):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee where e_name=? OR e_age=? OR e_salary=?", (e_name, e_age, e_salary))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_employee(id):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM employee where id=?", (id,))
    conn.commit()
    conn.close()


def update_employee(id, e_name, e_age, e_salary):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("UPDATE employee set e_name=?, e_age=?, e_salary=? WHERE id=?", (e_name, e_age, e_salary, id))
    conn.commit()
    conn.close()


connect()
