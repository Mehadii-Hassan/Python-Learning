academy = "10 Minute School"
#if use "10 Minute\nSchool." than output will be new line.
print(academy + "is cool.") #output will be "10 Minute School is cool."

print(academy.lower()) #output will be "10 minute school"
print(academy.upper()) #output will be "10 MINUTE SCHOOL"

print(academy.isupper()) #output will be False
print(academy.islower()) #output will be False

print(academy.upper().isupper()) #output will be True
print(academy.lower().islower()) #output will be True

print(len(academy)) #output will be 16, because there are 16 character with also blank space.

print(academy[0]) #output will be 1, because the first character is 1.
print(academy[4]) #output will be i, because the fourth character is i.
print(academy[3]) #output will be M, because the third character is M.

print(academy.index("S")) #output will be 10, because S is place 10.

print(academy.replace("10 Minute", "20 Hour")) #output will be "20 Hour School"