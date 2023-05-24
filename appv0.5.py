from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    con = sql.connect('Niila.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from USERS")
    data = cur.fetchall()
    return render_template("index.html", datas = data)

@app.route("/add_user", methods = ['POST', 'GET'])
def add_user():
    if request.method=='POST':
        NAME=request.form['NAME']
        SCORE=request.form['SCORE']
        con= sql.connect('Niila.db')
        cur = con.cursor()
        cur.execute("INSERT INTO USERS(NAME, SCORE) values (?,?), (NAME,SORE)")
        con.commit()
        flash('User Added', 'Success')
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:NAME>", methods =['POST', 'GET'])
def edit_user(uid):
    if request.method == 'POST':
        NAME = request.form['NAME']
        SCORE = request.form['SCORE']
        con = sql.connect('Niila.db')
        cur = con.cursor()
        cur.execute("UPDATE USERS SET NAME=?, SCORE=? WHERE UID=?", (NAME, SCORE, uid))
        con.commit()
        flash('USERS updated, success')
        return redirect(url_for('index'))
    con = sql.connect('Niila.db')
    con.row_factory= sql.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM USERS WHERE UID=?", (uid))
    data=cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:uid>", methods= ['GET'])
def delete_user(uid):
    con=sql.connect("Niila.db")
    cur = con.cursor()
    cur.execute("delete user from USERS where UID=?", (uid))
    con.commit()
    flash('User EXTERMINATED', 'Complete')
    return redirect(url_for("index"))

if __name__ == '__main__':
    #app.secret_key= 'admin123
    app.run