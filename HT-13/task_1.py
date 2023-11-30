"""
1. Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color з початковим значенням white і
метод для зміни кольору фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для
"""
class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

    def __str__(self):
        return f"Color: {self.color}"


class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def __str__(self):
        return f"Oval - Width: {self.width}, Height: {self.height}, {super().__str__()}"


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def __str__(self):
        return f"Square - Side Length: {self.side_length}, {super().__str__()}"


oval = Oval(5, 10)
print(oval)

square = Square(7)
print(square)
print("\n")

oval.change_color("blue")
square.change_color("red")

print(oval)
print(square)
