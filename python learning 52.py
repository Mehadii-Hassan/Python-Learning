class Shape: #parent class
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape): #child class (shape class er)
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
class Square(Shape): #child class (shape class er)
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
class Triangle(Shape): #child class (shape class er)
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(circle.color) #output - red
print(square.is_filled) #output - False
print(triangle.height) #output - 8