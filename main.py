import time
import greetings
from utilities import utilities
import requests
from requests import Response
from math import isclose

def main() -> None:

    print(time.sleep(1))  # this pauses the program for 1 second

    print(greetings.greet('Alice'))  # this greets Alice
    print(greetings.farewell('Alice'))  # this bids farewell to Alice

    # this prints the description of the greetings module
    print(greetings.DESCRIPTION)
    print(greetings.AUTHOR)  # this prints the author of the greetings module
    print(greetings.VERSION)  # this prints the version of the greetings module

    a: int = 2  # this is an integer variable
    b: int = 4  # this is another integer variable
    print(3 % 2)

    # this adds two integers using the add function from utilities module
    print(utilities.add(a, b))

    # this is a string variable containing a URL
    website: str = 'https://www.indently.io/abc'
    # this gets the response from the URL
    response: Response = get_response(website)
    show_response(response)  # this shows the response details

    # this is a dictionary containing user names and their ages
    users: dict = {'Alice': 25, 'Bob': 30, 'Norm': 29}
    if users:
        for user in users:
            print(f'User: {user}, Age: {users[user]}')
    else:
        print('Nor users were found')

    print(comparing_floats(0.1 + 0.2, 0.3))  # this compares two floats for equality


def get_response(url: str) -> Response:
    response = requests.get(url)
    return response


def show_response(response: Response) -> None:
    print('Status: ', response.status_code)
    print('OK: ', response.ok)
    print('Links: ', response.links)
    print('Encoding: ', response.encoding)
    print('Is redirect: ', response.is_redirect)
    print('Is perminate redirect: ', response.is_permanent_redirect)


def comparing_floats(a: float, b: float) -> bool:
    return isclose(a, b, rel_tol=.001)  # this compares two floats for equality


if __name__ == '__main__':
    main()  # this calls the main function to run the program
