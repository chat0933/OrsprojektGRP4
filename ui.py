# Make a UI that is easy to navigate

# 1: First option would be to connect to the server or close the program
# in the beginning make a version that does not connect to the internet
# But in the end it needs to connect to the internet

#1.5: Try to create the db with first function

# 2: Create a function that can write to a database keep it local first and then later try to make it work over the internet

# 3 Implement a function that makes changeing users possible

# 4 Implement threaing in all classes (Dropped)

# 5 use THE other dbs for UI instead of Niila db

import sqlite3
import ach_ide_3
#import user_database
import database


con = sqlite3.connect('database.db')
#achDB = AchiveDB
#achInsert = achiveinsert

###!!! VIGTIGT ÆNDRER USERNAME TIL TABLENAME FOR NEMMERE AT SENDE DATA IND!!!###

def ui():
    emptyUser = ""
    count = 1
    try:
        database.createUserDB()
        #ach_ide_3.AchiveDB()
        #app.runAPP()
        while True:
                with con:
                    cur= con.cursor()
                    print("Connecting to the server....")
                    print("Connection successful")
                    
                    if(count== 1):
                        print("in 1")
                        print('Hello', emptyUser)
                        print("Create a user on the website")
                    
                    elif(count== 2):
                         print("in 2")
                         print("Hello, the current Name logged in is of the user is:\n",createdUser())
                          
                    
                    #elif(count==3):
                         #print("in 3")
                         #print("Hello, the current ID, Name and Points of the user is:\n", createdUser())

                 # HERE WE NEED A FUNCTION THAT CAN UPDTAE THE CURRENT SCORE OF THE USERS
                 # FOUND THE UPDATING STATEMENT: "UPDATE USERS SET SCORE = X WHERE  ID = X"

                    elif(count==3):
                        print("NEEDS TO BE IMPLEMENTED")
                        print("Please enter the ID/NAME of which user you want to update:")
                        print("Hello", createdUser())
                        #print("Here is your updated score:")

                    print("Wellcome to Niila Games achivement scoreboard")
                    print(" Press 1 To register a new user(NOT WORKING ANYMORE)\n Press 2 to change the user\n Press 3 to update your progress (STILL IN DEVELEOPMENT!!!)\n Press Crtl+ c to exit the program")
                    print(" Enter the secret password to wipe the database")
                    menu = input()


                    if menu == "2":
                         print("Which user would you like to log in as instead")   
                         #uid = input("Please enter your ID: ")  
                         username = input("Please enter your name: ")
                         #password = input("TEST PASSWORD")
                         #There should be some sql statements that changes which row is in use 
                         # SELET FROM USER WHERE ID IS x
                         #IMPLEMENT A CURRENT SCORE SYSTEM
                         cur.execute("SELECT * FROM users WHERE username =(?)",[username])  
                         #def changedUser():
                              #changedUser= name
                              #return changedUser
                         count = 2

                    elif menu == "3":
                        #note IF THE INPUT DOES NOT MATCH THE ID AND NAME OF ANY SAVED ROW IN THE DB THE PROGRAM WILL CRASH
                        print("UPDATE YOUR SCORE TEST")
                        #uid = input("Please enter your ID: ")
                        Tablename = input("Please enter your name: ")
                        #cur.execute("UPDATE USERS SET SCORE= SCORE+ 10 WHERE ID=(?) AND NAME =(?)",(uid, name))
                        #print("WE NEED SOME MORE INPUTS THAT LETS US CHOSE THE ACHIVEMENT WE WANT TO ADD / ACTIVATE ")
                        bug_fixes = input("""Please enter how many bugs you have killed, Your options are:
9 or less bugs fixed
10 bugs fixed,
50 bugs fixed,
150 bugs fixed,
300 bugs fixed,
500 bugs fixed,
750 bugs fixed,
850 bugs fixed or
990 bugs fixed: \n""")
                        if bug_fixes == "9":
                            print("Good Job. You are close to earning an achivement")
                        elif bug_fixes == "10":
                             ach_ide_3.achiveinsert(11, Tablename)

                        elif bug_fixes == "50":
                             ach_ide_3.achiveinsert(51, Tablename)
                        
                        elif bug_fixes == "150":
                             ach_ide_3.achiveinsert(151, Tablename)
                        
                        elif bug_fixes == "300":
                             ach_ide_3.achiveinsert(301, Tablename)
                        
                        elif bug_fixes == "500":
                             ach_ide_3.achiveinsert(501, Tablename)
                        
                        elif bug_fixes == "750":
                             ach_ide_3.achiveinsert(751, Tablename)
                        
                        elif bug_fixes == "850":
                             ach_ide_3.achiveinsert(851, Tablename)
                        
                        elif bug_fixes == "990":
                             ach_ide_3.achiveinsert(991, Tablename)    
                       
                        else:
                             print("WRONG INPUT,try again")
                        
                            
                        count= 2
                        #return bug_fixes                                            
                    
                    elif menu == "admin":
                        print("Are you sure you would like to wipe the database of all its data?\n Press y if you want to delete all data, Press n if you don't want to wipe the database of all its data")
                        delete= input()
                        if delete == "y":
                            print("Database wiped")
                            #cur.execute("DELETE FROM USERS")
                            #con.commit()
                            #ach_ide_3.clearchivements()
                        elif delete == "n":
                            print("Returning to main menu....")

                    def createdUser():
                    #     selectedUserName = cur.execute("SELECT * FROM USERS WHERE ID =(?) AND NAME =(?) ",(uid,name))
                        selectedUserName = cur.execute("SELECT * FROM users WHERE username =(?) ",[username])
                        selectedUser = selectedUserName.fetchone()
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



               #NOTE dette er noget gammelt ui jeg lavede
                    # if menu == "1":
                    #      print("Enter your ID and Name")
                    # #    uid = input("Please ener your ID:\n")
                    #      username = input("Please enter your name:\n")
                    #      #startscore = 0
                    #      #Vi havde implementeret et score system men x fra Niial bad om at det ikke skulle være konkurence
                    # #     cur.execute("INSERT INTO USERS VALUES(?,?)",(username))
                    # #     con.commit()
                       
                    #      count = 2
