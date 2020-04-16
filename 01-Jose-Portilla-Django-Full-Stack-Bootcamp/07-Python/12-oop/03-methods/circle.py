class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, radius):
        self.radius = radius


circle = Circle(3)
print(circle.area())

circle.set_radius(10)
print(circle.area())

