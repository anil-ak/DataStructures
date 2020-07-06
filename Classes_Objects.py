

class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def Intro_Self(self):
        print('Hi There, Welcome to our site, My details: ')
        print(self.name)
        print(self.color)
        print(self.weight)
class Person:
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned
    def sitDown(self):
        self.isSitting = True
    def standUp(self):
        self.isSitting = False


print('Creating Objects...')
# Creating Object
TomRobot = Robot('tom','red', '30')
JerryRobot = Robot('jerry','blue', '40')

print('Using Methods...')
# Using method
TomRobot.Intro_Self()
JerryRobot.Intro_Self()

print('Relations...')
Person1 = Person('Alice', 'aggressive', False, JerryRobot)
Person1.robotOwned.Intro_Self()
Person2 = Person('Becky', 'talkative', True, JerryRobot)
Person2.robotOwned.Intro_Self()
Person2.robotOwned = TomRobot
Person2.robotOwned.Intro_Self()

print(Person1.isSitting)
Person1.sitDown()
print(Person1.isSitting)





