import random
import sys

# STEP 1: STARTING INFORMATION
print("Welcome to Rock, Paper, Scissors!")
moves: dict = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}
valid_moves: list = list(moves.keys())

# STEP 2: CREATE AN INFINITE LOOP
while True:

    # STEP 3: GET USER INPUT
    user_input: str = input(
        "Enter your move (rock, paper, scissors) or 'exit' to quit: ").lower()

    # STEP 4: CHECK FOR EXIT CONDITION
    if user_input == 'exit':
        print("Thanks for playing! Goodbye!")
        sys.exit()

    # STEP 5: VALIDATE USER INPUT
    if user_input not in valid_moves:
        print(f"Invalid move! Please choose from {', '.join(valid_moves)}.")
        continue

    # STEP 6: RANDOMLY SELECT COMPUTER MOVE
    computer_move: str = random.choice(valid_moves)
    print(f"Computer chose: {moves[computer_move]}")

    # STEP 7: DETERMINE WINNER
    if user_input == computer_move:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_move == 'scissors') or \
         (user_input == 'paper' and computer_move == 'rock') or \
         (user_input == 'scissors' and computer_move == 'paper'):
        print("You win!")
    else:
        print("You lose!")
