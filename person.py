# Create a simple class to represent a person
class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.age = 0

    def set_age(self, age):
        try:
            self.age = int(age)
        except:
            print("Invalid age")

    def speak(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}.")


# test code
p1 = Person("John", "Smith")
p1.speak()
p1.set_age(25)
print(p1.age)
p1.set_age("abc")