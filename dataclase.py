from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Fruit:

    name: str
    grams: float
    price_per_kg: float
    edible: bool = field(default=True)
    related_fruits: list[str] = field(default_factory=list)

    @property
    def total_price(self) -> float:
        """This code defines a property to check if the fruit is edible."""
        return (self.grams / 1000) * self.price_per_kg

    def describe(self) -> str:
        """This code defines a method to describe the fruit."""
        return f'{self.name} weighs {self.grams} grams and costs {self.total_price:.2f}.'


@dataclass
class Note:
    id: str = field(init=False)
    title: str
    body: str

    def __post_init__(self):
        """This code defines a post-initialization method to set a unique ID for the note."""
        self.id = str(uuid4())


def main():
    """This code defines a main function to create instances of the Fruit class and print their details."""
    apple = Fruit(name='Apple', grams=150, price_per_kg=3.0)
    banana = Fruit(name='Banana', grams=120, price_per_kg=1.5, related_fruits=['Apple'])
    orange = Fruit(name='Orange', grams=200, price_per_kg=2.0, edible=False, related_fruits=['Banana'])

    print(banana)
    print(orange)

    print(apple.describe())
    apple.price_per_kg = 3.5  # Update price per kg
    print(apple.describe())

    note = Note(title='Shopping List', body='Buy apples, bananas, and oranges.')
    print(note)


if __name__ == '__main__':
    main()
