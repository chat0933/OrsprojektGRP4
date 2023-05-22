# Make a UI that is easy to navigate

# 1: First option would be to connect to the server or close the program
# in the beginning make a version that does not connect to the internet
# But in the end it needs to connect to the internet
from Niladb import test

    
def bugspray():
    print("Congratz you have fixed five bugs today!!!")


def ui():
    while True:
        try:
            print("Connecting to the server....")
            print("Connection successful")

            print("Wellcome to Niila Games achivement scoreboard")


            
            print(" Press 1 view your acheviemnt score\n Press 2 to update your progress\n Press 3 to exit the program\n")

            menu = input()

            if menu == "1":
                print("Chose your user")

                #return(user)
            elif menu == "2":
                print("What would you like to update?\n")
                print("Press 1 if you fixed a bug")
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
                elif choice == "2":    
                    print('Going back to main menu')

            elif menu == "3":
                print("Closing the connection")
                SystemExit
        
        except ValueError:
            print("That is not a valid option\n Please try again")
            
ui()
test()
