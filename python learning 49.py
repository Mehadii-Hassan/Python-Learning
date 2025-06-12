class Student:

    class_year = 2023 #this line is class variable (we can access student 1 & 2)
    num_students = 0 #this line also class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Mehedi", 21)
student2 = Student("Sumaiya", 18)
student3 = Student("Rafi", 24)
student4 = Student("Moon", 20)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students") #output - My graduating class of 2023 has 4 students

print(student1.name) #output - Mehedi
print(student2.name) #output - Sumaiya
print(student3.name) #output - Rafi
print(student4.name) #output - Moon
