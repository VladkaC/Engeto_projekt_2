"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Vladěna Ceplechová
email: VladenaC@seznam.cz
"""

import random
import time
import textwrap

SEPARATOR = "-" * 45

def format_time(seconds):
    minutes = int(seconds // 60)
    sec = seconds % 60
    if minutes > 0:
        return f"{minutes} min {sec:.2f} s"
    else:
        return f"{sec:.2f} s"
    
def generate_random_number():
    numbers = random.sample(range(0, 9), 4)
    if numbers[0] == 0:
         numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers

def validate_input(user_input):
    if not user_input.isdigit():
        return "Input must contain only digits."
    elif len(user_input) != 4:
        return "Input must be exactly 4 digits."
    elif user_input[0] == "0":
        return "Number must not start with 0."
    elif len(set(user_input)) != 4:
        return "Digits must be unique."
    return None

def compare_numbers (random_numbers, user_numbers):
    str_user_numbers = str(user_numbers)
    bulls = 0
    cows = 0
    i = 0
    for number in random_numbers:
        if str(number) == str_user_numbers[i]:
            bulls += 1
        elif str(number) in str_user_numbers:
            cows += 1    
        i +=  1
    return bulls, cows

def play_game():
    guesses = 0
    start = time.time()
    four_random_numbers = generate_random_number()

    while True:
        user_numbers = input(">>>") 
        validation_error = validate_input(user_numbers)
        guesses += 1
        if validation_error:
            print(validation_error)
            continue
        
        bulls, cows = compare_numbers(four_random_numbers, user_numbers)

        if bulls == 4:
            end = time.time()
            second = end - start
            message = f"""
                >>>{user_numbers}
                Correct, you've guessed the right number
                in {guesses} guesses!
                {SEPARATOR}
                That's amazing!
                The game took {format_time(second)}
            """
            print(textwrap.dedent(message))
            break        
        else:
            print(f">>>{user_numbers}\n{bulls} bulls, {cows} cows\n")
            print(SEPARATOR)     
    return guesses   

print(textwrap.dedent(f"""
Hi there!
{SEPARATOR}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{SEPARATOR}
Enter a number:"""))

statistics = []

while True:
    guess = play_game()
    statistics.append(guess)

    again = input("Do you want to play again? (yes): ")

    if again.lower() != "yes":
        break
         
print("\nGame statistics:\n" + SEPARATOR)
for i, guess in enumerate(statistics, 1):
    print(f"Game {i:>2}: {guess} guesses")
print(SEPARATOR)
print(f"Best result : {min(statistics)} attempts")
print(f"Average     : {sum(statistics) / len(statistics):.2f} attempts")

