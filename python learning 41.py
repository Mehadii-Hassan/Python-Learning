#list comprehension = [expression for value in iterable if condition]
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles) #output - [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#example 1
fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

#example 2
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * 4 for z in range(1,11)]

#print(doubles)
#print(triples)
print(squares)

#example 3
numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_number = [num for num in numbers if num >= 0] #if no expression than just return the value
negative_number = [num for num in numbers if num <= 0]
even_number = [num for num in numbers if num % 2 == 0]
odd_number = [num for num in numbers if num % 2 != 0]

print(positive_number)
print(negative_number)
print(even_number)
print(odd_number)