import string

#
def is_letters_only(text: str) -> None:
    alphabet: str = string.ascii_letters + ' '

    for char in text:
        if char not in alphabet:
            raise ValueError(f'Invalid character "{char}" in input: "{text}"')

    print(f'Input "{text}" contains only letters and spaces.')


# Example usage
def main() -> None:
    while True:
        user_input = input('Enter text: ')

        if user_input.lower() in ['exit', 'quit']:
            print('Exiting the program. Goodbye!')
            break

        try:
            is_letters_only(user_input)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f'An unexpected error occurred: {type(e)} {e}')


if __name__ == '__main__':
    main()
