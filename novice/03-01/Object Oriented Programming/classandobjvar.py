class robot:
    """represents a robot, with a name."""
    population = 0
    def __init__(self, name):
        """initializes the data"""
        self.name = name
        print("(initializing {})".format(self.name))

        robot.population += 1
    def die(self):
        """i am dying."""
        print("{} is being destroyed!".format(self.name))

        robot.population -= 1

        if robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("there are still {:d} robots working.".format(robot.population))

    def say_hi(self):
        """greeting by the robot.
        yeah, they can do that."""
        print("greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """prints the current population."""
        print("we have {:d} robots.".format(cls.population))

droid1 = robot("R2-D2")
droid1.say_hi()
robot.how_many()

droid2 = robot("C-3PO")
droid2.say_hi()
robot.how_many()

print("\nrobots can do some work here.\n")

print("robots have finished their work. so let's destroy them.")
droid1.die()
droid2.die()

robot.how_many()