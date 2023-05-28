import sqlite3
# PRØV FØRST AT SØRGE FOR AT UID IKKE GÅR OVER 8

conn = sqlite3.connect("achievements.db")
cursor = conn.cursor()

class Achievement:
    def __init__(self, uid,  name, description):
        self.uid = uid
        self.name = name
        self.description = description
        # Hvorfor skal dette være false 
        self.completed = False

class Task:
    def __init__(self, name, description, achievements=[]):
        self.name = name
        self.description = description
        self.achievements = achievements or []

    def complete_achievement(self, uid, achievement_name):
        print("start")
        for achievement in self.achievements:
            if achievement.name == achievement_name:
                achievement.completed = True
            print(f"Achievement '{uid, achievement.name}' completed!")
            #return
        print(f"Achievement '{achievement_name}' not found for this task.")
              

def createTable():
    # Create achievements table
    print("ER I CREATE TABLE")
    cursor.execute("CREATE TABLE IF NOT EXISTS achievements (uid INTEGER PRIMARY KEY, name TEXT, description TEXT, completed INTEGER)")

def cleanDB():
    # Clear achievements
    cursor.execute("DELETE FROM achievements")

# Create achievements
achievement1 = Achievement(1,"Bug Spray", "Complete 10 bug fixes.")
achievement2 = Achievement(2,"Exterminator", "Complete 50 bug fixes")
achievement3 = Achievement(3,"The Duke of DEATH", "Complete 150 bug fixes.")
achievement4 = Achievement(4,"THANOS", "Complete 300 bug fixes")
achievement5 = Achievement(5,"BuggerFugger", "Complete 500 bug fixes")
achievement6 = Achievement(6,"ANTtomic bomb", "Complete 750 bug fixes")
achievement7 = Achievement(7,"Weapon of Moth Destruction", "Complete 1000 bug fixes")
achievement8 = Achievement(8,"The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes")

# Create a task with achievements
task1 = Task("Bug Spray", "Complete 10 bug fixes-task.", [achievement1])
task2 = Task("Exterminator", "Complete 50 bug fixes.", [achievement2])
task3 = Task("The Duke of DEATH", "Complete 150 bug fixes.", [achievement3])
task4 = Task("THANOS", "Complete 300 bug fixes.", [achievement4])
task5 = Task("BuggerFugger", "Complete 500 bug fixes", [achievement5])
task6 = Task("ANTtomic bomb", "Complete 750 bug fixes", [achievement6])
task7 = Task("Weapon of Moth Destruction", "Complete 1000 bug fixes", [achievement7])
task8 = Task("The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes", [achievement8])

def bugs():
    print("NEDE I BUGS")
    bug_fixes = 100
    print("...")
    # Complete an achievement
    if bug_fixes >= 10:
        task1.complete_achievement(1,"Bug Spray")
        fixed = 1

    if bug_fixes >= 50:
        task2.complete_achievement(2,"Exterminator")
        fixed = 2

    if bug_fixes >= 150:
        task3.complete_achievement(3,"The Duke of DEATH")
        fixed = 3

    if bug_fixes >= 300:
        task4.complete_achievement(4,"THANOS")
        fixed = 4
    
    if bug_fixes >= 500:
        task5.complete_achievement(5,"BuggerFugger")
        fixed = 5
    
    if bug_fixes >= 750:
        task6.complete_achievement(6,"ANTtomic bomb")
        fixed = 6
    
    if bug_fixes >= 1000:
        task7.complete_achievement(7,"Weapon of Moth Destruction")
        fixed = 7
    
    if bug_fixes >= 5000:
        task8.complete_achievement(8,"The Bug Banisher - Weaponizing marvellous disinfection")
        fixed = 8

    print("...")
    return fixed

def insert():
    print("NEDE I INSERT")
    fixed = bugs()
    # Insert achievements into the database
    if fixed >= 1:
        cursor.execute("UPDATE OR IGNORE achievements SET uid = 1")
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (NULL, ?, ?, ?)", (achievement1.name, achievement1.description, achievement1.completed))
        
    
    if fixed >= 2:
        cursor.execute("UPDATE OR IGNORE achievements SET uid = 2")
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (NULL, ?, ?, ?)", (achievement2.name, achievement2.description, achievement2.completed))
        
    
    if fixed >= 3:
        cursor.execute("UPDATE achievements SET uid = 3")
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (NULL, ?, ?, ?)" ,(achievement3.name, achievement3.description, achievement3.completed))
        
    if fixed >= 4:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (4, ?, ?, ?)",(achievement4.name, achievement4.description, achievement4.completed))
        cursor.execute("UPDATE achievements SET uid = 4"
                       )
    if fixed >= 5:
        cursor.execute("INSERT INTO achievements VALUES (NULL, ?, ?, ?)",(achievement5.name, achievement5.description, achievement5.completed))
        cursor.execute("UPDATE achievements SET uid = 5")
    if fixed >= 6:
        cursor.execute("INSERT INTO achievements VALUES (NULL, ?, ?, ?)",(achievement6.name, achievement6.description, achievement6.completed))
    
    if fixed >= 7:
        cursor.execute("INSERT INTO achievements VALUES (NULL, ?, ?, ?)" ,(achievement7.name, achievement7.description, achievement7.completed))
    
    if fixed >= 8:
        cursor.execute("INSERT INTO achievements VALUES (NULL, ?, ?, ?)",(achievement8.name, achievement8.description, achievement8.completed))

    conn.commit()


def testfunktion():
    createTable()
    bugs()
    insert()



# Update achievement status in the database
# for achievement in [achievement1, achievement2, achievement3, achievement4, achievement5, achievement6, achievement7, achievement8]:
#     cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (achievement.completed, achievement.name))
#     conn.commit()

# # Calculate the sum of completed values
# cursor.execute("SELECT SUM(completed) FROM achievements")
# sum_completed = cursor.fetchone()[0]

# Update the sum value in the database
#cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (sum_completed, "Total Completed"))
#conn.commit()

# Create total_completed table
#cursor.execute("CREATE TABLE IF NOT EXISTS total_completed (name TEXT, total INTEGER)")
# DELETE WARNING
#cursor.execute("DELETE FROM total_completed")

# Insert the sum of completed achievements into the total_completed table
#cursor.execute("INSERT INTO total_completed VALUES (?, ?)", ("Total Completed", sum_completed))

#conn.commit()
# Retrieve achievement status from the database
# cursor.execute("SELECT * FROM achievements")
# achievements = cursor.fetchall()

# Print achievement status
# for achievement in achievements:
#     uid, name, description, completed = achievement
#     print(f"UID: {uid}")
#     print(f"Achievement: {name}")
#     print(f"Description: {description}")
#     print(f"Status: {'Completed' if completed else 'Incomplete'}")
    #print()

#print(f"Achievement point sum: {sum_completed}")
print("...")

testfunktion()

#conn.close()