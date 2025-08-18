import time
from functools import cache


@cache
def count_vowels(text: str) -> int:
    '''Simulates an expensive computation by sleeping for 2 seconds.'''
    print(f'Counting for: {text}')
    time.sleep(5)
    return sum(text.count(vowel) for vowel in 'aeiouAEIOU')


def main() -> None:
    while True:
        user_input: str = input('You: Enter info, clear (or "exit" to quit): ').lower()
        if user_input == 'exit':
            break
        elif user_input == 'info':
            print(f'Bot: {count_vowels.cache_info()}')
        elif user_input == 'clear':
            count_vowels.cache_clear()
            print(f'Bot: cache has been cleared.')
        else:
            print(f'Bot: That text contains {count_vowels(user_input)} vowels')


if __name__ == '__main__':
    main()
