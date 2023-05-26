from flask import Flask, render_template
import sqlite3
import threading
app=Flask(__name__)
#MAKE A FUNCTION THAT RELOADS THE WEBPAGE, IT MIGHT BE JAVA SCRIPTS I NEED TO USE

con=("Niila.db")

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/USERS")
def USERS():
    print("EHJ")
    connect = sqlite3.connect(con)
    cur = connect.cursor()
    cur.execute("SELECT * FROM USERS")

    data = cur.fetchall()

    return render_template("users.html", data=data)


if __name__=='__main__':
    app.run(debug=False)