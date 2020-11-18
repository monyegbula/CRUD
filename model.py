import sqlite3 
from flask import redirect, url_for


#displayed the table 
def show_table():
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(""" SELECT * FROM employees ORDER BY pk DESC;""".format(name = name, email = email, phone = phone))
    table = cursor.fetchall()


    connection.commit()
    cursor.close()
    connection.close()
    return table

# inserted new data into table
def insert(name, email, phone):
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT name FROM employees WHERE email = '{email}';""".format(email = email))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute(
        """ INSERT INTO employees(
            name,
            email,
            phone
        )VALUES(
        '{name}',
        '{email}',
        '{phone}'
        );""".format(name = name, email = email, phone = phone)
        )


        connection.commit()
        cursor.close()
        connection.close()
       
    else:
        return('entry already exists!')
        

    return 'entry created succesfully!'


def employees():
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees;")
    myresult = cursor.fetchall()

    


    connection.commit()
    cursor.close()
    connection.close()

    return myresult

# updating table entries
def edit(name, email, phone, id):
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""UPDATE employees
        SET name= ?, email= ?, phone= ?
        WHERE id= ?
        )VALUES(
        '{name}',
        '{email}',
        '{phone}'
        );"""
        )
        
    

    connection.commit()
    cursor.close()
    connection.close()

    return ('entry updated succesfully')


def delete(id):
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?;", id)



    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('index'))


def check_pw(username):
    connection = sqlite3.connect('new_db.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM users WHERE username = '{username}' ORDER BY pk DESC;""".format(username = username))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password


def signup(username, password, color):
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""SELECT color FROM users WHERE username = '{username}';""".format(username = username))
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute(
        """ INSERT INTO users(
            username,
            password,
            color
        )VALUES(
        '{username}',
        '{password}',
        '{color}'
        );""".format(username = username, password = password, color = color)
        )


        connection.commit()
        cursor.close()
        connection.close()
       
    else:
        return('user already exists!')
        

    return 'user created succesfully!'

def check_users():
    connection = sqlite3.connect('new_db.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT username FROM users ORDER BY pk DESC;""")
    db_users = cursor.fetchall()
    users = []

    for i in range(len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()
    
    return users

def admin_pw(email):
    connection = sqlite3.connect('new_db.db', check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute("""SELECT password FROM admin WHERE email = '{email}' ORDER BY id DESC;""".format(email = email))
    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()
    return password

# admin user delete model
def userdelete(id):
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?;", id)



    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for('index'))

# users table
def users():
    connection = sqlite3.connect('new_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users;")
    newresult = cursor.fetchall()

    


    connection.commit()
    cursor.close()
    connection.close()

    return newresult