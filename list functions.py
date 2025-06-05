lucky_numbers = [42, 8, 15, 26, 23, 4]
friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.extend(lucky_numbers) #add two list together
print(friends) #output will be ['Khalid', 'Mainul', 'Rafi', 'Talha', 'Sakib']

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.append("Shanto") #add Shanto in friends
print(friends) #output will be ['Khalid', 'Mainul', 'Rafi', 'Talha', 'Sakib', 'Shanto']

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.insert(2, "Mahfuz") #push Mahfuz in index 2
print(friends) #output will be ['Khalid', 'Mainul', 'Mahfuz', 'Rafi', 'Talha', 'Sakib']

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.remove("Talha") #remove Talha in the list
print(friends) #output will be ['Khalid', 'Mainul', 'Rafi', 'Sakib']

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.clear() #remove all the list
print(friends) #output will be []

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.pop() #pop the last element
print(friends) #output will be ['Khalid', 'Mainul', 'Rafi', 'Talha']

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
print(friends.index("Mainul")) #output will be 1
print(friends.index("Talha")) #output will be 3

friends = ["Khalid", "Mainul", "Rafi", "Rafi", "Talha", "Sakib"] #this is a list of my friends
print(friends.count("Rafi")) #output will be 2, because Rafi is two time in the list

friends = ["Khalid", "Mainul", "Rafi", "Talha", "Sakib"] #this is a list of my friends
friends.sort() #maintain serial (letter wise)
print(friends) #output will be ['Khalid', 'Mainul', 'Rafi', 'Sakib', 'Talha']

lucky_numbers = [42, 8, 15, 26, 23, 4]
lucky_numbers.sort() #maintain serial (assending wise)
print(lucky_numbers) #output will be [4, 8, 15, 23, 26, 42]

lucky_numbers = [42, 8, 15, 26, 23, 4]
lucky_numbers.reverse() #back to front
print(lucky_numbers) #output will be [4, 23, 26, 15, 8, 42]

friends2 = friends.copy() #copy from friends variable
print(friends2) #output will be ['Khalid', 'Mainul', 'Rafi', 'Sakib', 'Talha']