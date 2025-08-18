import time
import logging


class Internet:
    def __init__(self, provider: str) -> None:
        self.provider = provider

    def connect(self) -> None:
        print(f'Connecting to {self.provider}...')
        time.sleep(2)
        print(f'Connected to {self.provider}.')


def dummy_connect() -> None:
    logging.warning(
        'This is a dummy connect function. No real connection will be made.')


def main() -> None:
    internet: Internet = Internet('ISP')
    internet.connect = dummy_connect
    internet.connect()


if __name__ == '__main__':
    main()
