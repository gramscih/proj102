my_area = 25

class Square:
    side_length = 2

    def calculate_square_area(self):
        print(my_area)
        return self.side_length ** 2

class Triangle:
    base_lenght = 4
    height = 3

    def calculate_triangle_area(self):
        print(my_area)
        return (0.5 * self.base_lenght) * self.height


def get_are(input_obj):
    if type(input_obj).__name__ =="Square":
        area = input_obj.calculate_square_area()
    elif type(input_obj).__name__ =="Triangle":
        area = input_obj.calculate_triangle_area()
    print(f"the Shape Are is {area}")


my_square = Square()
my_triangle = Triangle()

get_are(my_square)
get_are(my_triangle)

