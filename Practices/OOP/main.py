class Circle():
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return (self.radius**2)*Circle.pi

    def __str__(self):
        return "Radius is: {}".format(self.radius)

    def __del__(self):
        print("Circle of radius {} has been deleted".format(self.radius))

new_circle = Circle(4)
print(new_circle.get_area())
print(str(new_circle))