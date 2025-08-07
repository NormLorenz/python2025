from typing import Self


class Car:

    LIMITER: int = 200

    def __init__(self, brand: str, maxspeed: int) -> None:
        self.brand = brand
        self.maxspeed = maxspeed

    @classmethod
    def change_limiter(cls, new_limiter: int) -> None:
        cls.LIMITER = new_limiter

    @classmethod
    def autogenerate_max_speed(cls, brand: str) -> Self:
        if brand.lower() == 'bmw':
            return 290
        elif brand.lower() == 'toyota':
            return 280
        elif brand.lower() == 'volvo':
            return 300
        else:
            return 200

    def display_info(self) -> None:
        print(
            f'Brand: {self.brand}, Max Speed: {self.maxspeed} km/h, Speed Limiter: {self.LIMITER} km/h')


def main() -> None:
    # bmw = Car('BMW', 240)
    # toyota = Car('Toyota', 190)

    # bmw.display_info()
    # toyota.display_info()

    Car.change_limiter(150)

    # bmw.display_info()
    # toyota.display_info()

    volvo = Car('Volvo', Car.autogenerate_max_speed('Volvo'))
    volvo.display_info()
    bmw = Car('BMW', Car.autogenerate_max_speed('BMW'))
    bmw.display_info()
    toyota = Car('Toyota', Car.autogenerate_max_speed('Toyota'))
    toyota.display_info()
    chevrolet = Car('Chevrolet', Car.autogenerate_max_speed('Chevrolet'))
    chevrolet.display_info()


if __name__ == '__main__':
    main()
