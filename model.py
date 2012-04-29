'''
Created on 28/04/2012

@author: Jonathas Rodrigues <jonathas@archlinux.us>
'''

#from pysqlite2 import dbapi2 as sqlite
from sqlite3 import dbapi2 as sqlite
from os import path

class Sentences:
    
    def __init__(self):
        dbname = "qrcodegenerator.db"
        self.connection = sqlite.connect(dbname)
        self.cursor = self.connection.cursor()
        
        if path.getsize(dbname) == 0: # Oh, there's nothing there! :-O
            self.create_table()

    # Create the table in the database in order to receive the data
    def create_table(self):
        self.cursor.execute('CREATE TABLE sentences (id INTEGER PRIMARY KEY AUTOINCREMENT,sentence TEXT)')

    # Add sentence to the database
    def add(self, sentence):
        self.cursor.execute('INSERT INTO sentences VALUES (null, ?)', [sentence])
        self.connection.commit()
        
    def delete(self, del_id):
        self.cursor.execute('DELETE FROM sentences WHERE id = ?', [del_id])
        self.connection.commit()
        
    def select(self, select_id):
        self.cursor.execute('SELECT * FROM sentences WHERE id = ?', [select_id])
        row = self.cursor.fetchone()
        if hasattr(row, '__getitem__'):
            return row[1]
        else:
            return False

    def select_all(self):
        self.cursor.execute('SELECT * FROM sentences')
        rows = self.cursor.fetchall()
        if not rows:
            print "You don't have any sentence. Please insert one."
            return False
        
        for row in rows:
            print row[0], '-', row[1]
        return True
