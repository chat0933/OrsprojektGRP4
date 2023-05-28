import sqlite3

class Achievement:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

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
              
conn = sqlite3.connect("achievements.db")
cursor = conn.cursor()

def createachivementsDB():
    # Create achievements table
    print("Creating achivements database...")
    cursor.execute("CREATE TABLE IF NOT EXISTS achievements (name TEXT, description TEXT, completed INTEGER)")

def clearachivements():
    # Clear achievements
    print("Achivements cleared")
    cursor.execute("DELETE FROM achievements")
    conn.commit()

# Create achievements
achievement1 = Achievement("Bug Spray", "Complete 10 bug fixes.")
achievement2 = Achievement("Exterminator", "Complete 50 bug fixes")
achievement3 = Achievement("The Duke of DEATH", "Complete 150 bug fixes.")
achievement4 = Achievement("THANOS", "Complete 300 bug fixes")
achievement5 = Achievement("BuggerFugger", "Complete 500 bug fixes")
achievement6 = Achievement("ANTtomic bomb", "Complete 750 bug fixes")
achievement7 = Achievement("Weapon of Moth Destruction", "Complete 1000 bug fixes")
achievement8 = Achievement("The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes")




bug_fixes = 500
print("...")
# Complete an achievement
def completed():
    if bug_fixes >= 10:
        task1.complete_achievement("Bug Spray")
        bugsfixed = 1
        #return bugs 
    
    if bug_fixes >= 50:
        task2.complete_achievement("Exterminator")
        bugsfixed = 2
        #return bugs 
    
    if bug_fixes >= 150:
        task3.complete_achievement("The Duke of DEATH")
        bugsfixed = 3
        #return bugs 
    
    if bug_fixes >= 300:
        task4.complete_achievement("THANOS")
        bugsfixed = 4
        #return bugs 
    
    if bug_fixes >= 500:
        task5.complete_achievement("BuggerFugger")
        bugsfixed = 5
        #return bugs 
    
    if bug_fixes >= 750:
        task6.complete_achievement("ANTtomic bomb")
        bugsfixed = 6
        #return bugs 
    
    if bug_fixes >= 1000:
        task7.complete_achievement("Weapon of Moth Destruction")
        bugsfixed = 7 
    
    if bug_fixes >= 5000:
        task8.complete_achievement("The Bug Banisher - Weaponizing marvellous disinfection")
        bugsfixed = 8

    if bugsfixed <= 1:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement1.name, achievement1.description, achievement1.completed))
    elif bugsfixed <= 2:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement2.name, achievement2.description, achievement2.completed))
    elif bugsfixed <= 3:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement3.name, achievement3.description, achievement3.completed))
    elif bugsfixed <= 4:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement4.name, achievement4.description, achievement4.completed))
    elif bugsfixed <= 5:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement5.name, achievement5.description, achievement5.completed))
    elif bugsfixed <= 6:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement6.name, achievement6.description, achievement6.completed))
    elif bugsfixed <= 7:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement7.name, achievement7.description, achievement7.completed))
    elif bugsfixed <= 8:
        cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement8.name, achievement8.description, achievement8.completed))



# Insert achievements into the database


#conn.commit()

# Create a task with achievements
task1 = Task("Bug Spray", "Complete 10 bug fixes-task.", [achievement1])
task2 = Task("Exterminator", "Complete 50 bug fixes.", [achievement2])
task3 = Task("The Duke of DEATH", "Complete 150 bug fixes.", [achievement3])
task4 = Task("THANOS", "Complete 300 bug fixes.", [achievement4])
task5 = Task("BuggerFugger", "Complete 500 bug fixes", [achievement5])
task6 = Task("ANTtomic bomb", "Complete 750 bug fixes", [achievement6])
task7 = Task("Weapon of Moth Destruction", "Complete 1000 bug fixes", [achievement7])
task8 = Task("The Bug Banisher - Weaponizing marvellous disinfection", "Complete 5000 bug fixes", [achievement8])





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
#conn.commit()

# Create total_completed table
#cursor.execute("CREATE TABLE IF NOT EXISTS total_completed (name TEXT, total INTEGER)")
#cursor.execute("DELETE FROM total_completed")

# Insert the sum of completed achievements into the total_completed table
#cursor.execute("INSERT INTO total_completed VALUES (?, ?)", ("Total Completed", sum_completed))

conn.commit()

# Retrieve achievement status from the database
cursor.execute("SELECT * FROM achievements")
achievements = cursor.fetchall()

# Print achievement status
for achievement in achievements:
    name, description, completed = achievement
    print(f"Achievement: {name}")
    print(f"Description: {description}")
    print(f"Status: {'Completed' if completed else 'Incomplete'}")
    print()

print(f"Achievement point sum: {sum_completed}")
print("...")

#conn.close()
#clearachivements()
completed()
#insert()