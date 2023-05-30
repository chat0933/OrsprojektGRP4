import sqlite3
import user_database

class Achievement:
    def __init__(self, uid, name, description, times):
        self.uid = uid
        self.name = name
        self.description = description
        self.completed = False
        self.times = times

class Task:
    def __init__(self, name, description, achievements=[]):
        self.name = name
        self.description = description
        self.achievements = achievements or []

    def complete_achievement(self, achievement_name):
        for achievement in self.achievements:
            if achievement.name == achievement_name:
                achievement.completed = True
                print(f"Achievement '{achievement.name}' completed!")
                return
        print(f"Achievement '{achievement_name}' not found for this task.")
              
#conn = sqlite3.connect("achievements.db", check_same_thread= False)
conn = sqlite3.connect("user_data.db", check_same_thread= False)
cursor = conn.cursor()

# Create achievements table
def AchiveDB():
    cursor.execute("CREATE TABLE IF NOT EXISTS achievements (uid INTEGER PRIMARY KEY, name TEXT, description TEXT, completed INTEGER, times INTEGER)")

def deleteAchiveDB():
    # Clear achievements
    cursor.execute("DELETE FROM achievements")

# Create achievements
achievement1 = Achievement(1,"Bug Spray", "Complete 10 bug fixes.",1)
achievement2 = Achievement(2,"Exterminator", "Complete 50 bug fixes",1)
achievement3 = Achievement(3,"The Duke of DEATH", "Complete 150 bug fixes.",1)
achievement4 = Achievement(4,"THANOS", "Complete 300 bug fixes",1)
achievement5 = Achievement(5,"BuggerFugger", "Complete 500 bug fixes",1)
achievement6 = Achievement(6,"ANTtomic bomb", "Complete 750 bug fixes",1)
achievement7 = Achievement(7,"Weapon of Moth Destruction", "Complete 1000 bug fixes",1)
achievement8 = Achievement(8,"The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes",1)

conn.commit()

# Create a task with achievements
task1 = Task("Bug Spray", "Complete 10 bug fixes-task.", [achievement1])
task2 = Task("Exterminator", "Complete 50 bug fixes.", [achievement2])
task3 = Task("The Duke of DEATH", "Complete 150 bug fixes.", [achievement3])
task4 = Task("THANOS", "Complete 300 bug fixes.", [achievement4])
task5 = Task("BuggerFugger", "Complete 500 bug fixes", [achievement5])
task6 = Task("ANTtomic bomb", "Complete 750 bug fixes", [achievement6])
task7 = Task("Weapon of Moth Destruction", "Complete 1000 bug fixes", [achievement7])
task8 = Task("The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes", [achievement8])



print("...\n")

# DET VIRKER NU!!!!
def achiveinsert(bug_fixes, Tablename):
    user_database.createUserTable()
    if bug_fixes >= 10:  #or bug_fixes == 10:
        task1.complete_achievement("Bug Spray")
        #cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, ?)", (achievement1.uid, achievement1.name, achievement1.description, achievement1.completed, achievement1.times))
        #cursor.execute("UPDATE achievements SET times = times +1 WHERE uid ='1' ")        
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ?, ?, ?)", (achievement1.uid, achievement1.name, achievement1.description, achievement1.completed, achievement1.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times +1 WHERE uid ='1' ")
                


    if  bug_fixes >= 50: #bug_fixes == 50 or  :
        task2.complete_achievement("Exterminator")
        #cursor.execute("UPDATE achievements SET uid = 2")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, ?)", (achievement2.uid, achievement2.name, achievement2.description, achievement2.completed,achievement2.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='2' ")
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ?, ?, ?)", (achievement2.uid, achievement2.name, achievement2.description, achievement2.completed,achievement2.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times+1 WHERE uid ='2' ")

    if bug_fixes >= 150: # or bug_fixes == 150:
        task3.complete_achievement("The Duke of DEATH")
            #cursor.execute("UPDATE achievements SET uid = 3")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, ?)", (achievement3.uid, achievement3.name, achievement3.description, achievement3.completed,achievement3.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='3' ")    
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ?, ?, ?)", (achievement3.uid, achievement3.name, achievement3.description, achievement3.completed,achievement3.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times+1 WHERE uid ='3' ")             
    
    
    if bug_fixes >= 300: # or bug_fixes == 300:
        task4.complete_achievement("THANOS")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, ?)", (achievement4.uid, achievement4.name, achievement4.description, achievement4.completed, achievement4.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='4' ")
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ?, ?, ?)", (achievement4.uid, achievement4.name, achievement4.description, achievement4.completed, achievement4.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times+1 WHERE uid ='4' ")


    if bug_fixes >= 500:  #or bug_fixes == 500:
        task5.complete_achievement("BuggerFugger")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?,?)", (achievement5.uid ,achievement5.name, achievement5.description, achievement5.completed, achievement5.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='5' ")
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ?, ?,?)", (achievement5.uid ,achievement5.name, achievement5.description, achievement5.completed, achievement5.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times+1 WHERE uid ='5' ")

        
    if bug_fixes >= 750: # or bug_fixes == 750:
        task6.complete_achievement("ANTtomic bomb")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ? , ?, ?)", (achievement6.uid, achievement6.name, achievement6.description, achievement6.completed, achievement6.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='6' ")
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ? , ?, ?)", (achievement6.uid, achievement6.name, achievement6.description, achievement6.completed, achievement6.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times+1 WHERE uid ='6' ")
   
   
    #ORIGINAL 1000
    if bug_fixes >= 850: # or bug_fixes == 850:
        task7.complete_achievement("Weapon of Moth Destruction")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, ?)", (achievement7.uid, achievement7.name, achievement7.description, achievement7.completed, achievement7.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='7' ")
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}]  VALUES (?, ?, ?, ?, ?)", (achievement7.uid, achievement7.name, achievement7.description, achievement7.completed, achievement7.times))
        cursor.execute(f"UPDATE [{Tablename}]  SET times = times+1 WHERE uid ='7' ")


    #ORIGINAL 5000
    if bug_fixes >= 990: # or bug_fixes == 900:
        task8.complete_achievement("The Bug Banisher - Weaponizing marvellous disinfection")
        # cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, ?)", (achievement8.uid, achievement8.name, achievement8.description, achievement8.completed, achievement8.times))
        # cursor.execute("UPDATE achievements SET times = times+1 WHERE uid ='8' ")
        cursor.execute(f"INSERT OR IGNORE INTO [{Tablename}] VALUES (?, ?, ?, ?, ?)", (achievement8.uid, achievement8.name, achievement8.description, achievement8.completed, achievement8.times))
        cursor.execute(f"UPDATE [{Tablename}] SET times = times+1 WHERE uid ='8' ")        

        # Update achievement status in the database
    for achievement in [achievement1, achievement2, achievement3, achievement4, achievement5, achievement6, achievement7, achievement8]:
        #cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (achievement.completed, achievement.name))
        cursor.execute(f"UPDATE [{Tablename}] SET completed = ? WHERE name = ?", (achievement.completed, achievement.name))
        conn.commit()

    # Calculate the sum of completed values
    # cursor.execute("SELECT SUM(completed) FROM achievements")
    cursor.execute(f"SELECT SUM(completed) FROM [{Tablename}] ")
    sum_completed = cursor.fetchone()[0]

    # Update the sum value in the database
    # cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (sum_completed, "Total Completed"))
    cursor.execute(f"UPDATE [{Tablename}] SET completed = ? WHERE name = ?", (sum_completed, "Total Completed"))
    conn.commit()

    # Create total_completed table
    #cursor.execute("CREATE TABLE IF NOT EXISTS total_completed (name TEXT, total INTEGER)")
    #cursor.execute("DELETE FROM total_completed")

    # Insert the sum of completed achievements into the total_completed table
    #cursor.execute("INSERT INTO total_completed VALUES (?, ?)", ("Total Completed", sum_completed))

    conn.commit()

    # Retrieve achievement status from the database
    # cursor.execute("SELECT * FROM achievements")
    cursor.execute(f"SELECT * FROM [{Tablename}]")
    achievements = cursor.fetchall()

    # Print achievement status
    for achievement in achievements:
        uid,name, description, completed, times = achievement
        print(f"UID: {uid}")
        print(f"Achievement: {name}")
        print(f"Description: {description}")
        print(f"Status: {'Completed' if completed else 'Incomplete'}")
        print()

    #print(f"Achievement point sum: {sum_completed}")
    #print("...")
    print("...")

def CloseAch():
    conn.close()

#createDB()
#insert()

