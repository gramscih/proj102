class Shape:
    def calculate_area(self):
        pass

class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length ** 2

class Triangle(Shape):
    base_lenght = 4
    height = 3

    def calculate_area(self):
        return (0.5 * self.base_lenght) * self.height


def get_are(input_obj: Shape):
    area = input_obj.calculate_area()
    print(f"the Shape Are is {area}")


my_square = Square()
my_triangle = Triangle()

get_are(my_square)
get_are(my_triangle)

