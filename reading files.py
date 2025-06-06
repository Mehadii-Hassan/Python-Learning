employee_file = open("employees.txt", "r")

"""
print(employee_file.readable()) #output - True, because in line 1 it's read mode (r)
print(employee_file.readline()) #output - read individual one line, show the first line
print(employee_file.readline()) #output - read individual one line, show the first and second line

print(employee_file.read()) #output - show all the line
print(employee_file.readlines()) #output - show all information in a list
print(employee_file.readlines()[1]) #output - show the first element
"""
for employee in employee_file.readlines():
    print(employee)
employee_file.close()