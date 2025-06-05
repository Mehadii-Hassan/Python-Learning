def sayhi(): #define function
    print("Hi users")
sayhi() #calling function, output - Hi users

def sayhlw():
    print("Hello user")
print("Top")
sayhlw()
print("Bottom")
#output - Top than Hi user than Bottom

def say_hello(name):
    print("Hello " + name)
say_hello("Mehedi") #passing parameter, output - Hello Mehedi
say_hello("Hassan") #passing parameter, output - Hello Hassan

def say_hello(name, age):
    print("Hello " + name + "You are " + age)
say_hello("Mehedi, ", "22") #passing parameter, output - Hello Mehedi, You are 22
say_hello("Hassan, ", "25") #passing parameter, output - Hello Hassan, You are 25