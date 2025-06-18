class Animal: #grand class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal): #parents class
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal): #parents class
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): #child class
    pass

class Hawk(Predator): #child class
    pass

class Fish(Prey, Predator): #child class
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.sleep() #output - Bugs is sleeping
rabbit.eat() #output - Bugs is eating
rabbit.flee() #output - Bugs is fleeing
#rabbit.hunt() - for this the program showing error, because Rabbit is only child for Pray

hawk.sleep() #output - Tony is sleeping
hawk.eat() #output - Tony is eating
hawk.hunt() #output - Tony is hunting
#hawk.flee() - for this the program showing error, because Hawk is only child for Predator

fish.sleep() #output - Nemo is sleeping
fish.eat() #output - Nemo is eating
fish.flee() #output - Nemo is fleeing
fish.hunt() #output - Nemo is hunting

