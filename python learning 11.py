age = int(input("Enter your age: "))

if age >= 0 and age <= 17:
    print("You are under 18.")
elif age >= 18 and age <= 50 :
    print("Your are adult.")
else:
    print("You are old man")