import sqlite3

db = sqlite3.connect('db.sqlite')


def init():
    
    db.execute("""
         CREATE TABLE IF NOT EXISTS USER
         ( ID INT AUTO_INCREMENT PRIMARY KEY,
           IS_ADMIN INT NOT NULL,
           NAME VARCHAR(255) NOT NULL,
           EMAIL VARCHAR(255) NOT NULL,
           PASSWORD VARCHAR(255) NOT NULL,
           PHONENUMBER TEXT NOT NULL,
           PERMISSIONS TEXT NOT NULL
         )
    """)
    db.commit()
    pass
