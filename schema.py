import sqlite3

connection = sqlite3.connect('new_db.db', check_same_thread = False)
cursor = connection.cursor()




cursor.execute(
    """CREATE TABLE admin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(32),
        password VARCHAR(32)
    );"""

)

connection.commit()
cursor.close()
connection.close()

