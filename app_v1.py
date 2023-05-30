from flask import Flask, render_template
import sqlite3
import threading
import _thread
#import ui
app=Flask(__name__)
#MAKE A FUNCTION THAT RELOADS THE WEBPAGE, IT MIGHT BE JAVA SCRIPTS I NEED TO USE

conn= sqlite3.connect('Niila.db', check_same_thread= False)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/USERS")
def USERS():
    print("EHJ")
    #connect = sqlite3.connect(con, check_same_thread= False)
    cur = conn.cursor()
    cur.execute("SELECT * FROM USERS")

    data = cur.fetchall()

    return render_template("users.html", data=data)

def runAPP():
    while True:
        app.run(debug=True)

#def runUI():
    #while True:
        #try:
        #ui.ui()
        #except KeyboardInterrupt:
        #print("Close UI")


#runUI()

if __name__=='__main__':
    app.run(debug=False)
    #runUI()
    #runAPP()
            #runAPP()

            #print("close")
        