coordinates = (4, 5)
print(coordinates) #output will be (4, 5)
print(coordinates[0]) #output will be 4
print(coordinates[1]) #output will be 5

coordinates = [(4, 5), (6, 7), (80, 90)]
coordinates[1] = (10, 22)
print(coordinates) #output will be [(4, 5), (10, 22), (80, 90)]

#Note : Tuple item can't be change, but if I use list in tuple, than we can change the item.