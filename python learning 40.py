#Membership Operators = used to test whether a value or variable is found in a sequence
#                      (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

word = "APPLE"
letter = input("Guess a letter in the secret word: ")

#in
if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

#not in
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")
