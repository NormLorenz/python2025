from typing import Any

my_text: str = 'Bob'
my_list: list = [1, 2, 3]
my_int: int = 42
print('These are the globals:')
my_globals: dict[str, Any] = dict(globals())

for key, value in my_globals.items():
    if key.startswith('__') and key.endswith('__'):
        continue
    print(f'{key}: {value}')


def main() -> None:
    print('These are the locals:')
    my_name: str = 'Alice'
    my_age: int = 30
    my_tuple: tuple = (4, 5, 6)
    my_locals:  dict[str, Any] = dict(locals())

    for key, value in my_locals.items():
        if key.startswith('__') and key.endswith('__'):
            continue
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
