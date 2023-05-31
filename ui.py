import sqlite3
import ach_ide_3
import user_database
import database


con = sqlite3.connect('database.db')

def ui():
    emptyUser = ""
    count = 1
    try:
        database.createUserDB()
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


                    print("Wellcome to Niila Games achivement scoreboard")
                    print(" Press 1 To register a new user(NOT WORKING ANYMORE)\n Press 2 to change the user(YOU NEED TO USE THIS FUNCTION BEFORE USING UPDATING)\n Press 3 to update your progress (STILL IN DEVELEOPMENT!!!)\n Press Crtl+ c to exit the program")
                    print(" Enter the secret password to wipe the database")
                    menu = input()


                    if menu == "2":
                         print("Which user would you like to log in as instead")   
                         username = input("Please enter your name: ")
                         cur.execute("SELECT * FROM users WHERE username =(?)",[username])  
                         count = 2

                    elif menu == "3":
                        print("UPDATE YOUR SCORE TEST")
                        Tablename = input("Please enter your name: ")
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
                                                                   
                    
                    elif menu == "admin":
                        print("Are you sure you would like to wipe the database of all its data?\n Press y if you want to delete all data, Press n if you don't want to wipe the database of all its data")
                        delete= input()
                        if delete == "y":
                            print("Database wiped")
                            print("We need to implement a delete function")
                        elif delete == "n":
                            print("Returning to main menu....")

                    def createdUser():
                        selectedUserName = cur.execute("SELECT * FROM users WHERE username =(?) ",[username])
                        selectedUser = selectedUserName.fetchone()
                        return selectedUser

    except KeyboardInterrupt:
                print(" Closing the connection....")
                con.close
                ach_ide_3.CloseAch()
                user_database.closeUserTable()
                SystemExit
                    
ui()