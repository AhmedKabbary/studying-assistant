import sqlite3

db = sqlite3.connect('db.sqlite')


def init():
    db.execute("""
  CREATE TABLE IF NOT EXISTS DICTIONARY
    (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    WORD TEXT NOT NULL,
    DIFFICULTY INT NOT NULL)
    """)
    db.commit()

    pass
