from typing import TextIO

file_path: str = 'info.txt'

# file: TextIO = open(file_path, 'r')
# text: str = file.read()
# print(text)
# file.close()

try:
    with open(file_path, 'r') as file:  # Using 'with' to ensure the file is closed automatically
        text: str = file.read()
        print(text)

except FileNotFoundError:
    print(f'Error: The file {file_path} was not found.')

except IOError as e:
    print(f'Error: An I/O error occurred while accessing the file {file_path}. Details: {e}')

except Exception as e:
    print(f'An unexpected error occurred: {e}')