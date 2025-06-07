a = [1, 2, 3, 4, "a", 5, 6, 7, 8]

for i in a:
    if type(i) == type("b"):
        break #loop is stop here
    else:
        print(i)
        
print("-------------------")

for i in a:
    if type(i) == type("a"):
        continue #ignore the string
    else:
        print(i)