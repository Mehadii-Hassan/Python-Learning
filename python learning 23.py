#tuple = () ordered and unchangeable, duplicates ok, faster

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(len(fruits)) #output - 4
# print("apple" in fruits) #output - True
# print("pineapple" in fruits) #output - False

print(fruits.index("apple")) #output - 0
print(fruits.count("coconut")) #output - 2

#print(dir(fruits)) #what can we do - 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#print(help(fruits)) #description

#for fruit in fruits:
    #print(fruit) #output -

print(fruits) #output - {'apple', 'orange', 'banana', 'coconut'}
