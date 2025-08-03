import time
import greetings
from utilities import utilities
import requests
from requests import Response


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

    website: str = 'https://www.indently.io/abc'  # this is a string variable containing a URL
    response: Response = get_response(website)  # this gets the response from the URL
    show_response(response)  # this shows the response details


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


if __name__ == '__main__':
    main()  # this calls the main function to run the program
