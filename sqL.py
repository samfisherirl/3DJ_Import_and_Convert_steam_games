import sqlite3

con = sqlite3.connect('data.db')
cursor = con.cursor()

def create():
		
	# only needed once
	cursor.execute("create table games (game text, title text, steamid INTEGER, ubisoftid INTEGER, path text, exe text, base text)")

def insert():
	con.execute("INSERT INTO games VALUES('GTA', 'GTA', 'GTA.exe', 'id')") 

	con.commit()
#con.execute("SELECT * FROM games WHERE game='3D'") 
 
# cursor.executemany("insert into games values (?, ?, ?, ?)", release_list)


#for row in cursor.execute("select * from games"):#
	# all games
	#print(row)


cursor.execute("select * from games where exe=:c", {'c': 'mainmenu.exe'})
g = cursor.fetchall()
print(g)

con.commit()
con.close()

