menu = {
    "Biriyani": 150,
    "Chicken Curry": 120,
    "Beef Tehari": 180,
    "Paratha": 20,
    "Egg Toast": 30,
    "Vegetable Khichuri": 100,
    "Grilled Chicken": 200,
    "Mutton Rezala": 250,
    "Panta Ilish": 220,
    "Fuchka": 50
}

cart = []
total = 0

print("-------------MENU-------------")
for key, value in menu.items():
    print(f"{key:20} : {value} Tk")
print("------------------------------")

while True:
    food = input("Select item (q to quit): ")
    if food.lower() == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("Item not found in the menu. Please try again.")

print("-------------Your Order-------------")
for food in cart:
    total += menu.get(food)
    print(f"{food} - {menu.get(food)} Tk")

print(f"Total is: {total} Tk")