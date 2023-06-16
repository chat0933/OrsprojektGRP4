import sqlite3
import ach_ide_3 #Her ligger alle vores achivements og funktioner til dem
import ach_database #Her ligger vores achivement database
import user_database # Her ligger vores user database


con = sqlite3.connect('user_database.db')# Vi laver en instans af forbindelsen til databasen som vi giver variablen con

def ui(): #Vi opretter en funktion ved at bruge def, navnet til denne funktion hedder ui og er derfor gul
    emptyUser = "" #Variabel med tom string , kig på linje 22
    count = 1 # Vi sætter count til 1 fordi så gå den ned i vores if statement og printer hvad der står der
    try: # Dette gøres for at få exeptions til at virke, som er længere nede i koden (102)
        user_database.createUserDB() #Vi kører funktionen createUserDB fra mondulet user_database
        while True: #Vi laver en while true lykke for at programmet kører hele tiden indtil vi selv stopper det
                with con: # Vi forbinder til databasen ("ved" con virker linje 16)
                    cur= con.cursor() # her laver vi en funktion så vi kan ændrer i databasen.
                    print("Connecting to the server....")
                    print("Connection successful")
                    
                    if(count== 1): #Da vi har set count til at være 1 i linje 11 så starter vi herinde
                        print("in 1")
                        print('Hello', emptyUser) #Her bruges vores variabel fra linje 10 som indeholder en tom string, hvis der havde stået noget andet i "" så ville det stå der i stedet 
                        print("Create a user on the website")
                    
                    elif(count== 2): # Når count bliver sat til 2 længere nede i koden så bliver vores elif staement eksikveret i stedet for vores if statement
                         print("in 2")
                         print("Hello, the current Name logged in is of the user is:\n",createdUser()) #Denne funktion (createdUser laves nede i linje 97 til 100) \n er new line som gør at det næste stykke tekst er på næste linje


                    print("Wellcome to Niila Games achivement scoreboard")
                    print(" Press 1 To register a new user(NOT WORKING ANYMORE, USE THE WEBSITE TO REGISTER YOUR USER)\n Press 2 to change the user(YOU NEED TO USE THIS FUNCTION BEFORE USING UPDATING)\n Press 3 to update your progress\n Press Crtl+ c to exit the program")
                    print(" Enter the secret password to wipe the database (NOT WORKING CURRENTLY)")
                    menu = input() #Her laver vi en variabel som vi kalder for menu som er = input som er en funktion som tager input fra brugeren


                    if menu == "2": #Hivs man har indtastet 2 så ryger man ned i denne del af koden
                         print("Which user would you like to log in as instead")   
                         username = input("Please enter your name: ") #Her laver vi en variabel som er = input funktionen som tager input fra brugeren 
                         cur.execute("SELECT * FROM users WHERE username =(?)",[username]) #Her eksikveres der et cur.execute statement som kigger databasen igennem og leder efter username som vi har sat til ? som er tilsvarende vores input fra linje 38
                         count = 2

                    elif menu == "3":
                        print("UPDATE YOUR SCORE TEST")
                        Tablename = input("Please enter your name: ") # Her laver vi variablen Tablename som er = input funktionen der lader os skirve i terminalen
                        bug_fixes = input("""Please enter how many bugs you have killed, Your options are: 
9 or less bugs fixed
10 bugs fixed,
50 bugs fixed,
150 bugs fixed,
300 bugs fixed,
500 bugs fixed,
750 bugs fixed,
850 bugs fixed or
990 bugs fixed: \n""") #Fra linje 45: Igen laver vi en variabel med navn bug_fixes som er = input funktionen som lader os skrive i terminalen, her spørger den os om hvor mange bugs der er fixet
                        if bug_fixes == "9": #Fra linje 55- 79 kigger koden efter vores input og ud fra hvor mange bugs der er fixet så opdaterer den brugerens achivement progress
                            print("Good Job. You are close to earning an achivement")
                        elif bug_fixes == "10":
                             ach_ide_3.achiveinsert(11, Tablename) #Her er bug_fixes 11 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger

                        elif bug_fixes == "50":
                             ach_ide_3.achiveinsert(51, Tablename)#Her er bug_fixes 51 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger
                        
                        elif bug_fixes == "150":
                             ach_ide_3.achiveinsert(151, Tablename) #Her er bug_fixes 151 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger
                        
                        elif bug_fixes == "300":
                             ach_ide_3.achiveinsert(301, Tablename)#Her er bug_fixes 301 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger
                        
                        elif bug_fixes == "500":
                             ach_ide_3.achiveinsert(501, Tablename) #Her er bug_fixes 501 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger
                        
                        elif bug_fixes == "750":
                             ach_ide_3.achiveinsert(751, Tablename)#Her er bug_fixes 751 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger
                        
                        elif bug_fixes == "850":
                             ach_ide_3.achiveinsert(851, Tablename)#Her er bug_fixes 851 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger
                        
                        elif bug_fixes == "990":
                             ach_ide_3.achiveinsert(991, Tablename)#Her er bug_fixes 991 og vores tablename er det vi selv har indtastet i inje 44 så det vil sige at der ville tiløjes dette achivement en gang til den indtastede bruger    
                       
                        else:
                             print("WRONG INPUT,try again") #Smider os tilbage til lnije 25 hvis vi kommer til at indtaste forkerte oplysninger
                        count= 2
                                                                   
                    
                    elif menu == "admin": #Dette er et 'gemt' elif statement som lader os fjerne brugere fra databasen
                        #print("Are you sure you would like to wipe the database of all its data?\n Press y if you want to delete all data, Press n if you don't want to wipe the database of all its data")
                        print("Are you sure you would like to delte a user from the database?\n Press y if thats what you intenden\n Press n to abort the action")
                        delete= input() # Her sætter vi delete variablen = input funktion 
                        if delete == "y": #Hvis vi indtaster y så kører der en funktion som kan slette brugere fra databasen
                            #print("We need to implement a delete function")
                            ach_database.DropUserTable()
                            print("User deleted...")
                        elif delete == "n": # Hvis der bliver indtastet n så ryger vi tilbage på linje 25
                            print("Returning to main menu....")

                    def createdUser():
                        selectedUserName = cur.execute("SELECT * FROM users WHERE username =(?) ",[username]) #Her laver vi en varibel af det indtastede username fra linje 37 for at få vist det indtastede brugernavn når vi er i count 2/ vores elif statement
                        selectedUser = selectedUserName.fetchall() #Her laver vi en variabel af variablen selected user som anvender funktionen fetchall() som tager alt data fra det valgte row i dette tilfælde. Her er det brugernanv og password
                        return selectedUser #Selected user blive returneret så vi kan få vores navn ud i terminalen

    except KeyboardInterrupt:
                print(" Closing the connection....")
                con.close # Her lukkes forbindelsen til vores database
                #database.closeDatabase()
                ach_ide_3.CloseAch() #Her lukkes forbindelsen til achivement databasen
                ach_database.closeUserTable() #Her lukkes forbindelsen til vores user database
                #SystemExit
                    
ui()# Her kørers funktionen ui som er på linje 9