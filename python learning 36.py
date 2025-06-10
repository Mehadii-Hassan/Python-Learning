#example 1
def happy_birthday():
    print("Happy Birthday to you\n")
happy_birthday() #calling function

#example 2
def happy_birthdayy(name): #parameter
    print(f"Happy Birthday to {name}\n")
happy_birthdayy("Mehedi") #argument

#example 3
def happy_birthdayyy(name, age): #parameter
    print(f"Happy Birthday to {name}")
    print(f"You are {age} years old!\n")
happy_birthdayyy("Mehedi", 32) #argument

#example 4
def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(8,3))
print(subtract(8,3))
print(multiply(8,3))
print(divide(8,3))

#example 4
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("mehadi","hassan")
print(full_name)