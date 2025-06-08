#conditional expression:
#formula : X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

print("Positive" if num > 0 else "Negative")
print("Even" if num % 2 == 0 else "Odd")
print(a if a>b else b)
print(a if a<b else b)
print("Adult" if age >= 18 else "Child")
print("Hot" if temperature > 30 else "Cold")
print("Full access" if user_role == "admin" else "Limited access")