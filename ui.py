# Make a UI that is easy to navigate

# 1: First option would be to connect to the server or close the program
# in the beginning make a version that does not connect to the internet
# But in the end it needs to connect to the internet

#1.5: Try to create the db with first function

# 2: Create a function that can write to a database keep it local first and then later try to make it work over the internet

# 3 Implement a function that makes changeing users possible

# 4 Implement threaing in all classes 

import Niiladb
import sqlite3
import threading
import ach_ide_3

dbname= ('Niila.db')    
con = sqlite3.connect('Niila.db')

def ui():
    emptyUser = ""
    count = 1
    try:
        Niiladb.createDB()
        ach_ide_3.createachivementsDB()
        while True:
                with con:

                    cur= con.cursor()
                    print("Connecting to the server....")
                    print("Connection successful")
                    
                    if(count== 1):
                        print("in 1")
                        print('Hello', emptyUser)
                    
                    elif(count== 2):
                         print("in 2")
                         print("Hello, the current ID, Name and Points of the user is:\n",createdUser())
                        
                    
                    #elif(count==3):
                         #print("in 3")
                         #print("Hello, the current ID, Name and Points of the user is:\n", createdUser())


                 # HERE WE NEED A FUNCTION THAT CAN UPDTAE THE CURRENT SCORE OF THE USERS
                 # FOUND THE UPDATING STATEMENT: "UPDATE USERS SET SCORE = X WHERE  ID = X"

                    elif(count==3):
                        print("NEEDS TO BE IMPLEMENTED")
                        print("Please enter the ID/NAME of which users score you want to update:")
                        print("Hello", createdUser())
                        print("Here is your updated score:")

                    print("Wellcome to Niila Games achivement scoreboard")
                    print(" Press 1 To register a new user\n Press 2 to change the user\n Press 3 to update your progress (STILL IN DEVELEOPMENT!!!)\n Press Crtl+ c to exit the program")
                    print(" Enter the secret password to wipe the database")
                    menu = input()

                    if menu == "1":
                        print("Enter your ID and Name")
                        uid = input("Please ener your ID:\n")
                        name = input("Please enter your name:\n")
                        startscore = 0
                        cur.execute("INSERT INTO USERS VALUES(?,?,?)",(uid,name,startscore))
                        con.commit()
                       
                        count = 2

                    elif menu == "2":
                         print("Which user would you like to log in as instead")   
                         uid = input("Please enter your ID: ")  
                         name = input("Please enter your name: ")
                         #There should be some sql statements that changes which row is in use 
                         # SELET FROM USER WHERE ID IS x
                         #IMPLEMENT A CURRENT SCORE SYSTEM
                         #cur.execute("SELECT * FROM USERS WHERE ID =(?) AND NAME = (?)",(uid,name))  
                         #def changedUser():
                              #changedUser= name
                              #return changedUser
                         count = 2

                    elif menu == "3":
                        #note IF THE INPUT DOES NOT MATCH THE ID AND NAME OF ANY SAVED ROW IN THE DB THE PROGRAM WILL CRASH
                        print("UPDATE YOUR SCORE TEST")
                        uid = input("Please enter your ID: ")
                        name = input("Please enter your name: ")
                        print("TEST, GIVE 10 POINTS ")
                        cur.execute("UPDATE USERS SET SCORE= SCORE+ 10 WHERE ID=(?) AND NAME =(?)",(uid, name))
                        print("WE NEED SOME MORE INPUTS THAT LETS US CHOSE THE ACHIVEMENT WE WANT TO ADD / ACTIVATE ")
                        
                        count= 2
                                                                    
                    
                    elif menu == "admin":
                        print("Are you sure you would like to wipe the database of all its data?\n Press y if you want to delete all data, Press n if you don't want to wipe the database of all its data")
                        delete= input()
                        if delete == "y":
                            print("Database wiped")
                            cur.execute("DELETE FROM USERS")
                            con.commit()
                            #ach_ide_3.clearchivements()
                        elif delete == "n":
                            print("Returning to main menu....")

                    def createdUser():
                        selectedUserName = cur.execute("SELECT * FROM USERS WHERE ID =(?) AND NAME =(?) ",(uid,name))
                        selectedUser = selectedUserName.fetchall()
                        return selectedUser

    except KeyboardInterrupt:
                print(" Closing the connection....")
                con.close
                SystemExit
    except ValueError:
                print("That is not a valid option\n Please try again")
                    
ui()

# def NotUsedYet():
#                     elif menu == "99":
#                         print("What would you like to update?\n")
#                         print("Press 1 if you fixed a bug")
#                         print("Press 2 if you have helped your teamate")
#                         print("Press any other button to go back to the main menu")
#                         choice = input()
#                         if choice == "1": 
#                             print('How manny bugs have you killed today?')
#                             bugs = input()
#                             if bugs =="1":
#                                 print("Updating, you have fixd one bug today!!")
#                             elif bugs =="2":
#                                 print("Updating, you have fixd two bugs today!!")
#                             elif bugs == "3":
#                                 print("Updating, you have fixed three bugs today!!")
#                             elif bugs =="4":
#                                 print("Updating, you have fixed four bugs today!!\n Well done")
#                             elif bugs =="5":
#                                 print("Updating, you have fixed five bugs today!!!\n Well done, heres an achivement")
#                                 #bugspray()
#                                 #cur.execute("INSERT INTO u") note her skal der være to databaser som hver for deres data
                        
#                         elif choice == "2":    
#                             #Vi kan altid lave denen del om til en mere passende arbejdsopgave
#                             print('What did you help your teamate completing?')
#                             print(" Pres 1 i helped my teamate with x")
#                             print(" Pres 2 i helped my teamate with y")
#                             print(" Pres 3 i helped my teamate with z")
#                             help = input()
#                             if help == "1":
#                                 print("Hey good job, pat youself on the back")
#                             elif help == "2":
#                                 print("hejsa")
#                             elif help == "3":
#                                 print("Hejsa2 Godt klaret")