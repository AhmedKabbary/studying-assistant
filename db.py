import sqlite3

cursor = sqlite3.connect('db.sqlite')


def init():
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS USER
      	(
        	ID				INTEGER PRIMARY KEY AUTOINCREMENT,
        	IS_ADMIN 		BOOLEAN NOT NULL,
        	NAME 			TEXT NOT NULL,
			EMAIL 			TEXT NOT NULL,
			PASSWORD 		TEXT NOT NULL,
			PHONE 			TEXT NOT NULL,
			PERMISSIONS 	TEXT NOT NULL
		)
    """)
	
	cursor.execute("""
    	CREATE TABLE IF NOT EXISTS POMODOROS
     	(
			ID 				INTEGER PRIMARY KEY AUTOINCREMENT,
			DESCRIPTION 	TEXT NOT NULL,
      		CREATION_DATE 	TEXT NOT NULL,
			DONE 			BOOLEAN
		)
	""")
	
	cursor.execute("""
  		CREATE TABLE IF NOT EXISTS DICTIONARY
    	(
			ID 				INTEGER PRIMARY KEY AUTOINCREMENT,
    		WORD 			TEXT NOT NULL,
    		DIFFICULTY 		INTEGER NOT NULL
		)
    """)

	cursor.execute("""
	    CREATE TABLE IF NOT EXISTS TASKS
	    (
           ID 			     INTEGER PRIMARY KEY AUTOINCREMENT,
		   TASK              TEXT NOT NULL,
           CREATION_DATE     TEXT NOT NULL,
		   GROUP_ID          TEXT NOT NULL,
		   CHECKED			 BOOLEAN
	    )
	""")
	
	cursor.commit()


def is_table_empty(table_name):
    result = cursor.execute(f'SELECT COUNT(*) from {table_name}').fetchall()
    return (result[0][0] == 0)
