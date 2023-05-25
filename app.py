from flask import Flask, render_template
import sqlite3 as sql
app=Flask(__name__)

dbname=("Niila.db")

@app.route("/")
def db():
    print("EHJ")
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)