import sys
from datetime import datetime

def get_response(user_input: str) -> str:
    lowered = str.lower(user_input)

    if lowered in ['hi', 'hello', 'hey']:
        return 'Hey there!'

    elif 'how are you' in lowered:
        return 'I\'m good thanks for asking!'

    elif 'your name' in lowered:
        return 'My name is Bot :)'

    elif 'time' in lowered:
        current_time = datetime.now()
        return f'The time is: {current_time:%H:%M}'

    elif lowered in ['bye', 'goodbye']:
        return 'Goodbye! Have a great day! Bye'
    
    else:
        return f'Sorry, I didn\'t understand: "{user_input}"'
    


while True:
    user_input = input('You: ')
    
    if user_input.lower() in ['exit', 'quit']:
        print('Exiting the chatbot. Goodbye!')
        sys.exit()
    
    bot_response = get_response(user_input)
    print(f'Bot: {bot_response}')
    