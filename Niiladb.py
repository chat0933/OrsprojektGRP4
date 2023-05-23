import sqlite3
#Create a local database to test 
# Step two, move the database to a server 
# Step three, make a connection from python to the server with the database
# Make it in SQLIte
dbname = 'Niila.db'
con = sqlite3.connect('Niila.db')



with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS SCOREBOARD")
    #Drop table
    print("Table reset")
    cur.execute("CREATE TABLE SCOREBAORD(UID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, SCORE INT)")
    #Create users in database
    print("Database created")

con.commit()
con.close()

#createdb()
        

#Lav en drop table execution statement når vi åbner programmet


#Måske når vi sender ting til db så kan vi skrive en bruger har modtaget x antal af x achivemnt