class student:
    def __init__(self, name, dep, address, mobile):
        self.name = name
        self.dep = dep
        self.address = address
        self.mobile = mobile

student1 = student("Mehedi", "CSE", "Uttara", "017")
student2 = student("Mainul", "EEE", "CTG", "018")

print(student1.name)
print(student2.address)