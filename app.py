#import sqlite3
import user_database
import database
from flask import Flask, redirect, url_for, render_template, request, session


app = Flask(__name__)
app.secret_key = "protector"

#Den første side der åbner når vi runner flask
@app.route("/")
def index():
    return render_template('login.html')

#Her hvis "POST" er gældende vil if blokken kører (registrerer username og password), men hvis "GET" er gældende kører else blokken (åbner register.html)
#POST bruges til at submitte data, og GET bruges til at få data.
@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        database.register_user_to_db(username, password)
        return redirect(url_for('index'))
    else:
        return render_template('register.html')


#Hvis POST tjekker den om username og password er i databasen, hvis de er sender den til home, som er user.html, hvis ikke sender den til intruder.html.
@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if database.check_user(username, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('intruder.html')
    else:
        return redirect(url_for('index'))


#Hvis brugeren kan logge ind sender den brugeren til user.html som vil bruge den tilsvarende database/table.
@app.route('/home', methods=['POST', 'GET'])
def home():
    if 'username' in session:
        username = session['username']
        user_tables = user_database.get_user_tables()

        if username in user_tables:
            columns, rows = user_database.get_table_data(username)
            return render_template('user.html', username=username, columns=columns, rows=rows)
        else:
            return render_template('user.html', username=username, error=True)

    else:
        return redirect(url_for('index'))


#Logout når man klikker på logout knap, og sender en tilbage til login siden. 
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
