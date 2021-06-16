import sqlite3

conn = sqlite3.connect(':memory:')
weight = 25 #input('weight: ')
height = 50 #input('height: ')
data = (1, weight, height, 0)
conn.execute('CREATE TABLE "stocks"("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "weight", "height", "material_characteristics")')
conn.execute('SELECT * FROM "stocks"')
conn.execute('INSERT INTO "stocks"("id", weight, height, material_characteristics) '
             'VALUES(1, "weight", "height", 0)')

material =conn.execute('SELECT * FROM "stocks"').fetchall()
print(material)
cursor = conn.execute('SELECT * FROM "stocks";')
print(cursor.fetchone())
