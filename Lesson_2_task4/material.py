import sqlite3

conn = sqlite3.connect(':memory:')
c =conn.cursor()
weight = 25#input('weight: ')
height = 50#input('height: ')
c.execute('''
    INSERT INTO stocks
    ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    weight, 
    height, 
    material_characteristics)
    VALUES(?, ?, ?, ?), data
''')
data = (1, weight, height, 0)
