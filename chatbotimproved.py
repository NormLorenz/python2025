from difflib import get_close_matches


def get_best_match(user_question: str, knowledge: dict) -> str | None:

    questions: list[str] = [q for q in knowledge]
    matches: list[str] = get_close_matches(
        user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]

    return None


def run_chatbot(knowledge: dict) -> None:
    while True:
        user_input: str = input('You: ')
        if user_input.lower() == 'exit':
            print('Bot: Goodbye!')
            break

        best_match: str | None = get_best_match(user_input, knowledge)
        response: str | None = knowledge.get(best_match)

        if response:
            print(f'Bot: {response}')
        else:
            print('Bot: I\'m sorry, I don\'t know the answer to that question.')


if __name__ == '__main__':

    knowledge_base: dict[str, str] = {
        'What is your name?': 'I am a chatbot.',
        'How are you?': 'I\'m just a program, but thanks for asking!',
        'What can you do?': 'I can answer questions based on my knowledge base.',
        'Tell me a joke.': 'Why did the scarecrow win an award? Because he was outstanding in his field!',
        'What is the capital of France?': 'The capital of France is Paris.',
        'What is the meaning of life?': 'The meaning of life is subjective, but many say it is 42.',
        'What is Python?': 'Python is a programming language that lets you work quickly and integrate systems more effectively.',
        'What is the weather like today?': 'I\'m not sure, I don\'t have access to real-time data.',
        'What is the capital of Japan?': 'The capital of Japan is Tokyo.',
    }

    run_chatbot(knowledge_base)
