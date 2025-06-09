#example 1
fruits = [{"apple", "orange", "banana", "coconut"}]
vegetables = [{"celery", "carrots", "potatoes"}]
meats = [{"chicken", "fish", "turkey"}]

dinner_table = [fruits, vegetables, meats]

print(dinner_table) #output - [[{'banana', 'coconut', 'orange', 'apple'}], [{'carrots', 'celery', 'potatoes'}], [{'fish', 'turkey', 'chicken'}]]

#example 2
lunch_table = [{"apple", "orange", "banana", "coconut"},
               {"celery", "carrots", "potatoes"},
               {"chicken", "fish", "turkey"}]

for collection in lunch_table:
    for food in collection:
        print(food, end=" ")
    print()
