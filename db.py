import sqlite3

cursor = sqlite3.connect('db.sqlite')


def init():
    cursor.execute("""
		CREATE TABLE IF NOT EXISTS USER
      	(
        	ID			INTEGER AUTO INCREMENT PRIMARY KEY,
        	IS_ADMIN 	BOOLEAN NOT NULL,
        	NAME 		TEXT NOT NULL,
			EMAIL 		TEXT NOT NULL,
			PASSWORD 	TEXT NOT NULL,
			PHONE 		TEXT NOT NULL,
			PERMISSIONS TEXT NOT NULL
		)
    """)
    cursor.commit()


def is_table_empty(table_name):
    result = cursor.execute(f'SELECT COUNT(*) from {table_name}').fetchall()
    return (result[0][0] == 0)
