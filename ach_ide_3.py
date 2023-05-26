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

# Create achievements table
cursor.execute("CREATE TABLE IF NOT EXISTS achievements (name TEXT, description TEXT, completed INTEGER)")

# Clear achievements
cursor.execute("DELETE FROM achievements")

# Create achievements
achievement1 = Achievement("Bug Spray", "Complete 10 bug fixes.")
achievement2 = Achievement("Exterminator", "Complete 50 bug fixes")
achievement3 = Achievement("The Duke of DEATH", "Complete 150 bug fixes.")

# Insert achievements into the database
cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement1.name, achievement1.description, achievement1.completed))
cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement2.name, achievement2.description, achievement2.completed))
cursor.execute("INSERT INTO achievements VALUES (?, ?, ?)", (achievement3.name, achievement3.description, achievement3.completed))

conn.commit()

# Create a task with achievements
task1 = Task("Bug Spray", "Complete 10 bug fixes-task.", [achievement1])
task2 = Task("Exterminator", "Complete 50 bug fixes.", [achievement2])
task3 = Task("The Duke of DEATH", "Complete 150 bug fixes.", [achievement3])

bug_fixes = 187
print("...")
# Complete an achievement
if bug_fixes >= 10:
    task1.complete_achievement("Bug Spray")

if bug_fixes >= 50:
    task2.complete_achievement("Exterminator")

if bug_fixes >= 150:
    task3.complete_achievement("The Duke of DEATH")

print("...")

# Update achievement status in the database
for achievement in [achievement1, achievement2, achievement3]:
    cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (achievement.completed, achievement.name))
    conn.commit()

# Calculate the sum of completed values
cursor.execute("SELECT SUM(completed) FROM achievements")
sum_completed = cursor.fetchone()[0]

# Update the sum value in the database
cursor.execute("UPDATE achievements SET completed = ? WHERE name = ?", (sum_completed, "Total Completed"))
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

conn.close()