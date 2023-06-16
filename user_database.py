import sqlite3 #Vi importerer sqlite3 så vi kan tilgå og manipulerer databaser

#Dette ligger globalt så vi undgår at genbruge kode flere gange
con = sqlite3.connect('user_database.db', check_same_thread=False) #Vi laver en variabel af sqlite3 modulets funktion .connect, og indsætter to parametre heri. Det første er database navnet, og det næste er check_same_thread=False, som sørger for at SQL ikke tjekker om databasen er åben to steder på en gang, for ellers vil app.py koden ikke kører. 
cur = con.cursor() #Vi laver en variabel for en cursor som bruges til at placere sig i databasen, hvor man herfra kan manipulere databasen. 

def createUserDB(): #Vi definerer en funktion
    print("Creating User database") #simpel print funktion for vores skyld
    cur.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)') #Laver table for en bruger hvis det ikke eksisterer
    con.commit() #Den committer ændringer/gemmer ændringer. 

#Her laver vi en funktion der basically registrerer brugere ind i databasen
def register_user_to_db(username, password): #Vi definerer funktionen med to parametre.
    cur.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, password)) #Vi bruger execute funktionen til at indsætte værdierne username og password inde i database table users i user_database.db
    con.commit() #Den committer ændringer/gemmer ændringer.


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
