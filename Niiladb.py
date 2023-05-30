import sqlite3
#Create a local database to test 
# Step two, move the database to a server 
# Step three, make a connection from python to the server with the database
# Make it in SQLIte
#dbname = 'Niila.db'
con = sqlite3.connect('Niila.db')


def createDB():
    with con:
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY, NAME TEXT)")
        #, SCORE INT
        #Create users in database
        print("Database created")

    con.commit()
    #con.close()

#createDB()