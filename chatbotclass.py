from random import choice
from datetime import datetime


class Chatbot:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_description(self) -> str:
        return f'{self.name} is a chatbot who is {self.age} years old.'

    def get_responses(self, text: str) -> str:
        lowered: str = text.lower()
        if 'hello' in lowered:
            return f'{self.name}: Hey there!'
        elif 'bye' in lowered:
            return f'{self.name}: See you!'
        elif 'how old are you' in lowered:
            return f'{self.name}: I am {self.age} years old'
        elif 'what time is it' in lowered:
            return f'{self.name}: The current time is {datetime.now().strftime("%H:%M:%S")}'
        elif 'how are you' in lowered:
            return f'{self.name}: Great thanks for asking!'
        else:
            random_responses: list[str] = [
                f'I am not sure how to respond to that.',
                f'Can you please rephrase?',
                f'I did not understand that.'
                f'Ah, what?',
                f'I am still learning, please be patient.'
            ]
            return f'{self.name}: {choice(random_responses)}'

    def run(self) -> None:
        print(f'Welcome to the chatbot named {self.name}!')
        print('Type "bye" to exit the chat.')
        while True:
            user_input: str = input('You: ')
            if user_input.lower() == 'bye':
                print(f'{self.name}: Goodbye!')
                break
            response: str = self.get_responses(user_input)
            print(response)


def main() -> None:
    chatbot: Chatbot = Chatbot('Norm', 23)
    print(chatbot.get_description())
    chatbot.run()


if __name__ == '__main__':
    main()
