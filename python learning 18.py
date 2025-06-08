#example 1
for x in range(1, 21):
    print(x) #output 1-20

#example 2
for x in range(1, 21, 2):
    print(x) #output 1 3 5 7 .... 15 17 19

#example 3
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x) #output 1-12

#example 4
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x) #output 1-20 without 13