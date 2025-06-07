# {}
# unordered
#no update
#no duplicates

a = {1,2,2,3,4,4,4,5}
s = set(a)
print(s) #don't print duplicate value {1, 2, 3, 4, 5}

#union and intersection
a = {1,2,3}
b = {2,3,4}

c = a.intersection(b)
d = a.union(b)
print(a) #Output - {1, 2, 3}
print(b) #Output - {2, 3, 4}