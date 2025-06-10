#scope resolution = (LEGB) local > enclosed > global > built-in
#example for local
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1() #function block er moddhe value thakle local
func2()

#example for enclosed
def func1():
    x = 1
    def func2():
        print(x)
    func2()
func1() #sub function block a kono value na thakle root er value check kore sheta print korbe, eta k enclosed bole

#example for global
def func1():
    print(x)

def func2():
    print(x)

x = 3 #eta function block er bahire value dewa tai eta global

func1()
func2()

#example for built-in
from math import pi
def func1():
    print(pi)
func1() 