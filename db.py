import sqlite3

cursor = sqlite3.connect('db.sqlite')


def init():
    cursor.execute("""
    	CREATE TABLE IF NOT EXISTS POMODOROS
     	(
			ID INTEGER INT PRIMARY KEY AUTOINCREMENT,
			DESCRIPTION TEXT NOT NULL,
      		CREATION_DATE TEXT NOT NULL,
			DONE BOOLEAN
		)
	""")
    
    cursor.execute("""
  		CREATE TABLE IF NOT EXISTS DICTIONARY
    	(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
    		WORD TEXT NOT NULL,
    		DIFFICULTY INT NOT NULL
		)
    """)

    cursor.commit()
