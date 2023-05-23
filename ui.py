# Make a UI that is easy to navigate

# 1: First option would be to connect to the server or close the program
# in the beginning make a version that does not connect to the internet
# But in the end it needs to connect to the internet

    
def bugspray():
    print("You have unlocked the achivement 'Bug Sprayer!!'")


def ui():
    try:
        while True:
            print("Connecting to the server....")
            print("Connection successful")

            print("Wellcome to Niila Games achivement scoreboard")
            print(" Press 1 view your acheviemnt score\n Press 2 to update your progress\n Press Crtl+ c to exit the program\n")

            menu = input()

            if menu == "1":
                print("Chose your user")
                #Make a connction to db
                #return(user)
            elif menu == "2":
                print("What would you like to update?\n")
                print("Press 1 if you fixed a bug")
                print("Press 2 if you have helped your teamate")
                print("Press 2 to go back to the main menu")
                choice = input()

                if choice == "1": 
                    print('How manny bugs have you killed today?')
                    bugs = input()
                    if bugs =="1":
                        print("Updating, you have fixd one bug today!!")
                    elif bugs =="2":
                        print("Updating, you have fixd two bugs today!!")
                    elif bugs == "3":
                        print("Updating, you have fixed three bugs today!!")
                    elif bugs =="4":
                        print("Updating, you have fixed four bugs today!!\n Well done")
                    elif bugs =="5":
                        print("Updating, you have fixed five bugs today!!!\n Well done, heres an achivement")
                        bugspray()
                elif choice == "3":    
                    #Vi kan altid lave denen del om til en mere passende arbejdsopgave
                    print('What did you help your teamate completing?')
                    print(" Pres 1 i helped my teamate with x")
                    print(" Pres 2 i helped my teamate with y")
                    print(" Pres 3 i helped my teamate with z")
                    help = input()
                    if help == "1":
                        print("Hey good job, pat youself on the back")
                    if help == "2":
                        print("hejsa")
                    if help == "3":
                        print
    except KeyboardInterrupt:
        print("Closing the connection....")
        SystemExit
    except ValueError:
        print("That is not a valid option\n Please try again")
            
ui()