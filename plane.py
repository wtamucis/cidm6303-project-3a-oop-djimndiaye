# Code a class that describe planes following the instructions. 
# We are just simulating a simple plane. You can imagine 
# these methods could control a plane's functionality
class Plane:
    def __init__(self, given_name):
        self.empty_weight = 0
        self.engines = 2
        self.make = ""
        self.model = ""
        self.name = given_name
        self.speed = 0
        self.wing_span = 0

    def throttle_engine(self, amount):
        self.speed = self.speed + amount
        print(f"{self.name} speed is now {self.speed}")

    def pitch(self, degree):
        print(f"{self.name} pitches {degree} degrees")

    def roll(self, degrees):
        print(f"{self.name} rolls {degrees} degrees")


# test code
plane1 = Plane("Falcon")
plane1.throttle_engine(50)
plane1.pitch(10)
plane1.roll(30)
