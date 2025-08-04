import sys


def welcome() -> None:
    print('Welcome to the Grocery Store!')
    print('Enter:')
    print('-' * 10)
    print('1 - to add a new grocery item')
    print('2 - to remove a grocery item')
    print('3 - to list all grocery items')
    print('4 - to exit the program')
    print('-' * 10)


def add(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f'Added {item} to the grocery list.')


def remove(item: str, groceries: list[str]) -> None:
    if item in groceries:
        groceries.remove(item)
        print(f'Removed {item} from the grocery list.')
    else:
        print(f'{item} not found in the grocery list.')


def list(groceries: list[str]) -> None:
    if groceries:
        print('Grocery List:')
        for item in groceries:
            print(f'- {item}')
    else:
        print('The grocery list is empty.')


def validate_choice(choice: str) -> bool:
    return choice in {'1', '2', '3', '4'}


def main() -> None:
    groceries: list[str] = []
    welcome()

    while True:
        choice = input('Enter your choice: ')
        if not validate_choice(choice):
            print('Invalid choice. Please try again.')
            continue

        if choice == '1':
            item = input('Enter the grocery item to add: ')
            add(item, groceries)
        elif choice == '2':
            item = input('Enter the grocery item to remove: ')
            remove(item, groceries)
        elif choice == '3':
            list(groceries)
        elif choice == '4':
            print('Exiting the program. Goodbye!')
            sys.exit(0)


if __name__ == '__main__':
    main()
