#List = [] ordered and changeable, duplicates ok

fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[2]) #output - banana
# print(fruits[:3]) #output - ['apple', 'orange', 'banana']
# print(fruits[::2]) #output - ['apple', 'banana']
# print(fruits[::-1]) #output - ['coconut', 'banana', 'orange', 'apple']
# print(len(fruits)) #output - 4
# print(fruits.index("apple")) #output - 0
# print(fruits.count("banana")) #output - 1
# print("apple" in fruits) #output - True
# print("pineapple" in fruits) #output - False

#fruits[0] = "pineapple" #output - ['pineapple', 'orange', 'banana', 'coconut']

#fruits.append("pineapple") #output - ['apple', 'orange', 'banana', 'coconut', 'pineapple']
#fruits.remove("apple") #output - ['orange', 'banana', 'coconut']
#fruits.insert(0, "pineapple") #output - ['pineapple', 'apple', 'orange', 'banana', 'coconut']
#fruits.sort() #output - ['apple', 'banana', 'coconut', 'orange']
#fruits.reverse() #output - ['coconut', 'banana', 'orange', 'apple']
#fruits.clear() #output - []

#print(dir(fruits)) #what can we do - 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
#print(help(fruits)) #description

#for fruit in fruits:
    #print(fruit) #output -

print(fruits) #output - ['apple', 'orange', 'banana', 'coconut']
