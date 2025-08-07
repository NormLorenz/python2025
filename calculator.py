class Calculator:
    def __init__(self, version: int = 1) -> None    :
        self.version = version

    @staticmethod
    def add(*numbers: float) -> float:
        return sum(numbers)


def main() -> None:
    calc = Calculator()
    result = calc.add(1.5, 2.5, 3.0)
    print(f'The version of calculator is {calc.version}')
    print(f'The result of the addition is: {result}')
    result2 = Calculator.add(4.0, 5.0, 6.0)
    print(f'The result of the static addition is: {result2}')

if __name__ == '__main__':
    main() 

 