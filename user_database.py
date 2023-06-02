import sqlite3

#Dette ligger globalt så vi undgår at genbruge kode flere gange
con = sqlite3.connect('user_database.db', check_same_thread=False)
cur = con.cursor()

def createUserDB():
    print("Creating User database")
    cur.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    con.commit()

#Her laver vi en funktion der basically registrerer brugere ind i databasen
def register_user_to_db(username, password):
    cur.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password))
    con.commit()


#Her tjekker vi om username og password der bliver indtastet stemmer overens med databasen. 
def check_user(username, password):
    cur.execute('SELECT username, password FROM users WHERE username=? AND password=?', (username, password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False
    
def closeDatabase():
    con.close()
