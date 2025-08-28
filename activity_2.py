# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves")

# Child classes with different move() behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Base class for Animals
class Animal:
    def move(self):
        print("The animal moves")

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]
animals = [Dog(), Fish(), Bird()]

print("Vehicles:")
for v in vehicles:
    v.move()

print("\nAnimals:")
for a in animals:
    a.move()
