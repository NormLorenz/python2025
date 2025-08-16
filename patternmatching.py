user_input: str = input('Enter a string: ')
command: list[str] = user_input.split()

match command:
    case 'find', *images:
        print(f'Finding images: {images}...')
    case 'enlarge', image, amount:
        print(f'Enlarging image {image} by {amount}...')
    case 'shrink', image, amount:
        print(f'Shrinking image {image} by {amount}...')
    case 'rotate', image, angle:
        print(f'Rotating image {image} by {angle} degrees...')
    case 'rename', image, new_name if len(new_name) > 3:
        print(f'Renaming image {image} to {new_name}...')
    case 'x' | 'delete', *images:
        print(f'Images deleted: {images}...')
    case _:
        print('Unknown command. Please try again.')