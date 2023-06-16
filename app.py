#import sqlite3
import ach_database #Vi importerer et selvskabt modul, så vi kan bruge funktionerne der er indeni
import user_database #Vi importerer et selvskabt modul, så vi kan bruge funktionerne der er indeni
from flask import Flask, redirect, url_for, render_template, request, session #Vi importerer Flask klassen fra flask modulet samt funktionerne redirect_ url_for, render_template, og variablerne request, session. 


app = Flask(__name__) #Initialiserer app.py filen
app.secret_key = "protector" #Brugt til at beskytte session data. 


user_database.createUserDB() #Henter og kalder funktionen createUserDB fra vores modul user_database, som laver: CREATE USER DATABASE IF NOT EXISTS

#Den første side der åbner når vi runner flask
@app.route("/") #Vi laver en decorator/endpoint med URL stien "/" som gør at det er den første side der åbnes når man kører flask
def index(): #vi definerer en funktion
    return render_template('login.html') #Returnerer render_template() funktionen fra flask modulet, som viser login.html filen

#Her hvis "POST" er gældende vil if blokken kører (registrerer username og password), men hvis "GET" er gældende kører else blokken (åbner register.html)
#POST bruges til at submitte data, og GET bruges til at få data.
@app.route('/register', methods=["POST", "GET"]) #Laver endpoint med metoderne POST og GET (POST = indsætte data)(GET = hente data)
def register(): #Definerer funktion
    if request.method == 'POST': #Et if statement som siger at hvis request variablens metode er POST, vil kodeblokken under eksekveres.
        username = request.form['username'] #Laver en variabel for den data vi får fra HTML-siden. Specifikt fra data med navnet username
        password = request.form['password'] #Laver en variabel for den data vi får fra HTML-siden. Specifikt fra data med navnet password

        user_database.register_user_to_db(username, password) #kalder funktion fra user_database modulet, hvor vi bruger variablerne username og password som vi LIGE har lavet (linje 23 og 24)
        return redirect(url_for('index')) #returnerer redirect funktionen med funktionen url_for som videresender dig til URL'et for index. Teknisk set kunne vi have lavet et render_template("login.html") i stedet her.
    else:
        return render_template('register.html') #Else statement for at lukke if statement af, så den fungerer. Egentlig i sig selv gør den ikke andet end det. 



@app.route('/login', methods=["POST", "GET"]) #App.route som checker om username og password findes i databasen, hvis de gør leder den til /home app.routen, hvis username og password ikke findes, sender den brugeren til html siden intruder.html.
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_database.check_user(username, password):
            session['username'] = username
            return redirect(url_for('home')) #Den fører IKKE til home.html (vi bruger faktisk slet ikke home.html) den fører istedet til app.routen /home, som starter i linje 49.
        else:
            return render_template('intruder.html')
    else:
        return redirect(url_for('index'))


#Hvis brugeren kan logge ind sender den brugeren til user.html som vil bruge den tilsvarende database/table.
@app.route('/home', methods=['POST', 'GET']) #dapp.route(decorator) '/home'(endpoint) methods(variabel) 
def home(): #definerer funktion home
    if 'username' in session: #checker om 'username' er gemt i session objektet.
        username = session['username'] #Hvis 'username' findes i sessions objektet, henter den så værdien for 'username' og gemmer det som variablen username 
        user_tables = ach_database.get_user_tables() #Her laves en variabel som kalder på funktionen get_user_tables() fra modulet ach_database

        if username in user_tables: #if statement som checker om hvis værdien 'username' som er gemt i sessions objektet, som er gemt som variabel username, er i user_tables vil kodeblokken eksekveres.
            columns, rows = ach_database.get_table_data(username) #Her kalder vi funktionen get_table_data fra modulet ach_database, hvor vi giver funktionen argumentet username, for så at få columns og rows fra det tilsvarende table.
            return render_template('user.html', username=username, columns=columns, rows=rows) #Her returnerer vi et rendered HTML template, user.html, og videregiver username, columns og rows, så det kan bruges til dynamisk HTML.
        else:
            return render_template('user.html', username=username, error=True) #Her returnerer vi et rendered HTML template, user.html, men med variablen error sat til True, som vi så kan bruge til at displaye en besked på html-siden. 

    else:
        return redirect(url_for('index'))


#Logout når man klikker på logout knap, og sender en tilbage til login siden. 
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

