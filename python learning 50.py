class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def run(self):
        print(f"{self.name} is running")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Roky")
cat = Cat("Pukie")
mouse = Mouse("Mickey")

print(dog.name) #output - Roky
print(cat.name) #output - Pukie
print(mouse.name) #output - Mickey

dog.sleep() #output - Roky is sleeping
cat.eat() #output - Pukie is eating
mouse.run() #output - Mickey is running

dog.speak() #output - WOOF!
cat.speak() #output - MEOW!
mouse.speak() #output - SQUEEK!