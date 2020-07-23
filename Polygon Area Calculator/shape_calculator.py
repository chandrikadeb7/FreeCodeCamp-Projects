class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ''
            for _ in range(0, self.height):
                picture += "*" * self.width + '\n'
            return picture

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def get_amount_inside(self, shape):
        times = 0
        if (shape.width < self.width) and (shape.height < self.height):
            times = (self.height // shape.height) * (self.width // shape.width)
            return times
        else:
            times = 0
            return times


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def set_width(self, side):
        super(Square, self).set_width(side)

    def set_height(self, side):
        super(Square, self).set_height(side)

    def __str__(self):
        return f"Square(side={self.side})"
