class Achievement:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False

class Task:
    def __init__(self, name, description, achievements=[]):
        self.name = name
        self.description = description
        self.achievements = achievements

    def complete_achievement(self, achievement_name):
        for achievement in self.achievements:
            if achievement.name == achievement_name:
                achievement.completed = True
                print(f"Achievement '{achievement.name}' completed!")
                return
        print(f"Achievement '{achievement_name}' not found for this task.")

# Create achievements
achievement1 = Achievement("Bug Spray", "Complete 10 bug fixes.")
achievement2 = Achievement("Exterminator", "Complete 50 bug fixes")
achievement3 = Achievement("The Duke of DEATH", "Complete 150 bug fixes.")

# Create a task with achievements
task = Task("Bug Spray-Task.", "Complete 10 bug fixes-task.", [achievement1])
task = Task("Exterminator-Task.", "Complete 50 bug fixes.", [achievement2])
task = Task("The Duke of DEATH-Task", "Complete 150 bug fixes.", [achievement3])



bug_fixes = 160
# Complete an achievement

if bug_fixes >= 10 and bug_fixes < 50:
    task.complete_achievement("Bug Spray")
elif bug_fixes >= 50 and bug_fixes <= 150:
    task.complete_achievement("Exterminator")
elif bug_fixes >= 150:
    task.complete_achievement("The Duke of DEATH")
    
# Check achievement status
for achievement in task.achievements:
    print(f"Achievement: {achievement.name}")
    print(f"Description: {achievement.description}")
    print(f"Status: {'Completed' if achievement.completed else 'Incomplete'}")
    print()
    