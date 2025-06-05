day_conversions = {
    "Sat": "Saturday",
    "Sun": "Sunday",
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thu": "Thursday",
    "Fri": "Friday"
}
print(day_conversions) #output - {'Sat': 'Saturday', 'Sun': 'Sunday', 'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thu': 'Thursday', 'Fri': 'Friday'}
print(day_conversions["Mon"]) #output - Monday
print(day_conversions.get("Fri")) #output - Friday
print(day_conversions.get("Luv")) #output - None

month_conversions = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(month_conversions) #output - {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
print(month_conversions[5]) #output - May
print(month_conversions.get(11)) #output - November
print(month_conversions.get(13)) #output - None