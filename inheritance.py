class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_mutton(self):
        print("The chef makes a mutton")


class ChineseChef(Chef): #using (Chef) all the function copy here from Chef class
    def make_fried_rice(self):
        print("The chef makes fried rice")


myChef = Chef()
myChef.make_chicken() #output - The chef makes a chicken
myChef.make_salad() #output - The chef makes a salad
myChef.make_mutton() #output - The chef makes a mutton

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice() #output - The chef makes fried rice
myChineseChef.make_salad() #output - The chef makes a salad
myChineseChef.make_mutton() #output - The chef makes a mutton
myChineseChef.make_chicken() #output - The chef makes a chicken