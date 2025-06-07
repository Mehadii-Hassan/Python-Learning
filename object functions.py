class Student:
    def __init__(self, name, dep, gpa):
        self.name = name
        self.dep = dep
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

student1 = Student("Mehedi", "CSE", 3.11)
student2 = Student("Mainul", "EEE", 3.74)

print(student2.on_honor_roll()) #output - True