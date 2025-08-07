from abc import ABC, abstractmethod


class Appliance(ABC):

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.version = model
        self.is_turned_on: bool = False

    @abstractmethod
    def turn_on(self) -> None:
        '''Turn on the appliance.'''
        pass

    @abstractmethod
    def turn_off(self) -> None:
        '''Turn off the appliance.'''
        pass


class Microwave(Appliance):
    def __init__(self, brand: str, model: str) -> None:
        super().__init__(brand, model)
        self.is_turned_on = False

    def turn_on(self) -> None:
        self.is_turned_on = True
        print(f'{self.brand} microwave model {self.version} is now ON.')

    # def turn_off(self) -> None:
    #     self.is_turned_on = False
    #     print(f'{self.brand} microwave model {self.version} is now OFF.')

    def turn_off(self) -> None:
        raise NotImplementedError("This method is not implemented yet.")


def main() -> None:
    microwave = Microwave('Samsung', 'MW1234')
    microwave.turn_on()
    microwave.turn_off()


if __name__ == '__main__':
    main()
