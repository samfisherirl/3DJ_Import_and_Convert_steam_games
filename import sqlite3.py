import sqlite3

con = sqlite3.connect('data.db')
cursor = con.cursor()

# only needed once
# cursor.execute("create table games (game text, title text, exe text, id text)")


con.execute("INSERT INTO games VALUES('GTA', 'GTA', 'GTA.exe', 'id')") 

con.commit()
con.execute("SELECT * FROM games WHERE game='3D'")

print(cursor.fetchall())

release_list = [ 
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"),
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"),
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"),
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"),
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"),
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"),
("3D Armada (2016)", "3D Armada", "mainmenu.exe", "9zXDFHvBvVlXOk"), ]

cursor.executemany("insert into games values (?, ?, ?, ?)", release_list)


for row in cursor.execute("select * from games"):
	# all games
	print(row)


cursor.execute("select * from games where exe=:c", {'c': 'mainmenu.exe'})
g = cursor.fetchall()
print(g)

con.commit()
con.close()

