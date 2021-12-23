import sqlite3

db = sqlite3.connect('db.sqlite')


def init():
    
    db.execute("""CREATE TABLE IF NOT EXISTS pomo_tasks
     (id INT AUTO_INCREMENT PRIMARY KEY, description VARCHAR(100),
      creation_date VARCHAR(10), done BIT)""")
    
    db.commit()