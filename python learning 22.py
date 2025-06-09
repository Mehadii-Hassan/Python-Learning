#set = {} unordered and immutable, but add/remove ok, no duplicates

fruits = {"apple", "orange", "banana", "coconut"}

# print(len(fruits)) #output - 4
# print("apple" in fruits) #output - True
# print("pineapple" in fruits) #output - False

#fruits.add("pineapple") #output - {'apple', 'banana', 'pineapple', 'coconut', 'orange'}
#fruits.remove("apple") #output - {'orange', 'banana', 'coconut'}
#fruits.clear() #output - set()
#fruits.pop() #output - {'apple', 'coconut', 'orange'}

#print(dir(fruits)) #what can we do - 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#print(help(fruits)) #description

#for fruit in fruits:
    #print(fruit) #output -

print(fruits) #output - {'apple', 'orange', 'banana', 'coconut'}
