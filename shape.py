from typing import override


class Shape (object):
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def describe(self) -> None:
        print(f'This is a {self.name} with {self.sides} sides.')

    def shape_method(self) -> None:
        print(f'Performing a shape-specific operation for {self.name}.')


class Square(Shape):
    def __init__(self, size: float) -> None:
        super().__init__('Square', 4)
        self.size = size

    @override
    def describe(self) -> None:
        print(f'I am a square {self.name} with size {self.size}')


class Rectangle(Shape):
    def __init__(self, length: float, height: float) -> None:
        super().__init__('Rectangle', 4)
        self.length = length
        self.height = height

    @override
    def describe(self) -> None:
        print(
            f'I am a rectangle {self.name} with length {self.length} and a height of {self.height}')


def main() -> None:
    square: Square = Square(20)
    square.describe()
    square.shape_method()

    rectangle: Rectangle = Rectangle(10, 5)
    rectangle.describe()
    rectangle.shape_method()


if __name__ == '__main__':
    main()
