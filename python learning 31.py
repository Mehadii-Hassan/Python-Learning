#dictionary = {key:value} ordered and changeable. no duplicates

capitals = {
    "Bangladesh" : "Dhaka",
    "India" : "New Delhi",
    "Russia" : "Moscow",
    "China" : "Beijing",
    "USA" : "Washington D.C"
}

# print(dir(capitals)) #what can we do
# print(help(capitals)) #discription

# print(capitals.get("Bangladesh")) #output - Dhaka
# print(capitals.get("Japan")) #output - None

#capitals.update({"Germany" : "Berlin"}) #output - {'Bangladesh': 'Dhaka', 'India': 'New Delhi', 'Russia': 'Moscow', 'China': 'Beijing', 'USA': 'Washington D.C', 'Germany': 'Berlin'}
#capitals.update({"USA" : "Detroit"}) #output - {'Bangladesh': 'Dhaka', 'India': 'New Delhi', 'Russia': 'Moscow', 'China': 'Beijing', 'USA': 'Detroit'}
#capitals.pop("China") #output - {'Bangladesh': 'Dhaka', 'India': 'New Delhi', 'Russia': 'Moscow', 'USA': 'Washington D.C'}
#capitals.popitem() #output - {'Bangladesh': 'Dhaka', 'India': 'New Delhi', 'Russia': 'Moscow', 'China': 'Beijing'}
#capitals.clear() #output - {}

"""
if capitals.get("Bangladesh"):
    print("The capital is exists")
else:
    print("The capital doesn't exist")  
#output - The capital is exists

keys = capitals.keys()
#print(keys) #output - dict_keys(['Bangladesh', 'India', 'Russia', 'China', 'USA'])
for key in keys:
    print(key)

values = capitals.values()
#print(values) #output -  dict_values(['Dhaka', 'New Delhi', 'Moscow', 'Beijing', 'Washington D.C'])
for value in values:
    print(value)

items = capitals.items()
#print(items) #output -   dict_items([('Bangladesh', 'Dhaka'), ('India', 'New Delhi'), ('Russia', 'Moscow'), ('China', 'Beijing'), ('USA', 'Washington D.C')])
for key, value in capitals.items():
    print(f"{key} : {value}")
"""
print(capitals) #output - {'Bangladesh': 'Dhaka', 'India': 'New Delhi', 'Russia': 'Moscow', 'China': 'Beijing', 'USA': 'Washington D.C'}
