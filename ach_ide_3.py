import sqlite3
#x = 1
class Achievement:
    def __init__(self, uid, name,description, times):
        self.uid = uid
        self.name = name
        self.description = description
        self.completed = False
        self.times = times
        

class Task:
    def __init__(self, uid, name, description ,times, achievements=[]):
        self.uid = uid
        self.name = name
        self.description = description
        #self.complted = completed
        self.times = times
        self.achievements = achievements or []

    def complete_achievement(self, uid,achievement_name, times):
        for achievement in self.achievements:
            if achievement.name == achievement_name:
                achievement.completed = True
                uid = [1,2,3,4,5,6,7,8]
                times = times +1
                print(f"Achievement '{achievement.name}' completed!")
                return
        print(f"Achievement '{achievement_name}' not found for this task.")
              
conn = sqlite3.connect("achievements.db")
cursor = conn.cursor()

def createachivementsDB():
    # Create achievements table
    print("Creating achivements database...")
    cursor.execute("CREATE TABLE IF NOT EXISTS achievements (uid INTEGER PRIMARY KEY, name TEXT, description TEXT, completed INTEGER, times INTEGER)")

def clearachivements():
    # Clear achievements
    print("Achivements cleared")
    cursor.execute("DELETE FROM achievements")
    conn.commit()

# Create achievements
achievement1 = Achievement(1,"Bug Spray", "Complete 10 bug fixes.",None)
achievement2 = Achievement(2,"Exterminator", "Complete 50 bug fixes", None)
achievement3 = Achievement(3,"The Duke of DEATH", "Complete 150 bug fixes.",None)
achievement4 = Achievement(4,"THANOS", "Complete 300 bug fixes",None)
achievement5 = Achievement(5,"BuggerFugger", "Complete 500 bug fixes",None)
achievement6 = Achievement(6,"ANTtomic bomb", "Complete 750 bug fixes",None)
achievement7 = Achievement(7,"Weapon of Moth Destruction", "Complete 1000 bug fixes",None)
achievement8 = Achievement(8,"The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes",None)

# Create a task with achievements
task1 = Task("Bug Spray", "Complete 10 bug fixes-task.",None,[achievement1])
task2 = Task("Exterminator", "Complete 50 bug fixes.", None,[achievement2])
task3 = Task("The Duke of DEATH", "Complete 150 bug fixes.",None, [achievement3])
task4 = Task("THANOS", "Complete 300 bug fixes.",None, [achievement4])
task5 = Task("BuggerFugger", "Complete 500 bug fixes",None, [achievement5])
task6 = Task("ANTtomic bomb", "Complete 750 bug fixes",None, [achievement6])
task7 = Task("Weapon of Moth Destruction", "Complete 1000 bug fixes",None, [achievement7])
task8 = Task("The Bug Banisher - Weaponizing marvellous disinfection","Complete 5000 bug fixes", None, [achievement8])


bug_fixes = 310
print("...")
# Complete an achievement
def completedAch():
    if bug_fixes >= 10:
        task1.complete_achievement(1,"Bug Spray",True)
        bugs = 1
        #return bugs
    
    if bug_fixes >= 50:
        task2.complete_achievement(2,"Exterminator",True)
        bugs = 2
        #return bugs
    
    if bug_fixes >= 150:
        task3.complete_achievement(3,"The Duke of DEATH",True)
        bugs =3
        #return bugs
    
    if bug_fixes >= 300:
        task4.complete_achievement(4,"THANOS",True)
        bugs = 4
        #return bugs
    
    if bug_fixes >= 500:
        task5.complete_achievement(5,"BuggerFugger",True)
        bugs = 5
        #return bugs
    
    if bug_fixes >= 750:
        task6.complete_achievement(6,"ANTtomic bomb",True)
        bugs = 6
        #return bugs
    
    if bug_fixes >= 1000:
        task7.complete_achievement(7,"Weapon of Moth Destruction",True)
        bugs = 7
        #return bugs
    
    if bug_fixes >= 5000:
        task8.complete_achievement(8,"The Bug Banisher - Weaponizing marvellous disinfection",True)
        bugs = 8
    
    return bugs


# Insert achievements into the database
def insert():
    bugs = completedAch()
    #x = 1
    if bugs >= 1:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (1,achievement1.name, achievement1.description, achievement1.completed))
        #achievement1.times
        #cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 1")
    
    if bugs >= 2:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (2, achievement2.name, achievement2.description, achievement2.completed))
        #cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 2")
    
    if bugs >= 3:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (3, achievement3.name, achievement3.description, achievement3.completed))
        cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 3")
    
    if bugs >= 4:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (4, achievement4.name, achievement4.description, achievement4.completed))
        cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 4")
    
    if bugs >= 5:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (5, achievement5.name, achievement5.description, achievement5.completed))
        cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 5")
    
    if bugs >= 6:
       cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (6, achievement6.name, achievement6.description, achievement6.completed))
       cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 6") 
    
    if bugs >= 7:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (7, achievement7.name, achievement7.description, achievement7.completed))
        cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 7")
    
    if bugs >= 8:
        cursor.execute("INSERT OR IGNORE INTO achievements VALUES (?, ?, ?, ?, NULL)", (8, achievement8.name, achievement8.description, achievement8.completed))
        cursor.execute("UPDATE achievements SET times = times +1 WHERE uid = 8")

def testfunction():
        createachivementsDB()
        completedAch()
        insert()

#conn.commit()
testfunction()

print("...")

# Update achievement status in the database
for achievement in [achievement1, achievement2, achievement3, achievement4, achievement5, achievement6, achievement7, achievement8]:
    cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (achievement.completed, achievement.name))
    conn.commit()

# Calculate the sum of completed values
cursor.execute("SELECT SUM(completed) FROM achievements")
sum_completed = cursor.fetchone()[0]

# Update the sum value in the database
cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (sum_completed, "Total Completed"))
conn.commit()

# Create total_completed table
cursor.execute("CREATE TABLE IF NOT EXISTS total_completed (name TEXT, total INTEGER)")
cursor.execute("DELETE FROM total_completed")

# Insert the sum of completed achievements into the total_completed table
cursor.execute("INSERT INTO total_completed VALUES (?, ?)", ("Total Completed", sum_completed))

conn.commit()

# Retrieve achievement status from the database
cursor.execute("SELECT * FROM achievements")
achievements = cursor.fetchall()

# Print achievement status
for achievement in achievements:
    uid, name, description, completed, times = achievement
    print(f"Uid: {uid}")
    print(f"Achievement: {name}")
    print(f"Description: {description}")
    print(f"Status: {'Completed' if completed else 'Incomplete'}")
    print(f'Times completed: {times}')
#print(f"Achievement point sum: {sum_completed}")
print("...")
