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
    """
    Converts time in seconds to a human-readable string format.
    """
    minutes = int(seconds // 60)
    sec = seconds % 60
    if minutes > 0:
        return f"{minutes} min {sec:.2f} s"
    else:
        return f"{sec:.2f} s"
    

def generate_secret_number():
    """
    Generates a 4-digit number with unique digits that does not start with 0.
    """
    numbers = random.sample(range(0, 10), 4)
    if numbers[0] == 0:
         numbers[0], numbers[1] = numbers[1], numbers[0]
    return numbers


def validate_input(user_input):
    """
    Validates user input to ensure it is a 4-digit number with unique digits and doesn't start with 0.
    Returns None if valid, otherwise an error message string.
    """
    if not user_input.isdigit():
        return "Input must contain only digits."
    elif len(user_input) != 4:
        return "Input must be exactly 4 digits."
    elif user_input[0] == "0":
        return "Number must not start with 0."
    elif len(set(user_input)) != 4:
        return "Digits must be unique."
    return None


def compare_numbers(random_numbers, user_input):
    """
    Compares the secret number and user's input.
    Returns the number of bulls (correct digit & position) and cows (correct digit, wrong position).
    """
    bulls = 0
    cows = 0

    for i, number in enumerate(random_numbers):
        if str(number) == user_input[i]:
            bulls += 1
        elif str(number) in user_input:
            cows += 1

    return bulls, cows


def play_game(input_function=input, output_function=print):
    """
    Runs one round of the Bulls and Cows game.
    Returns the number of guesses the player took.
    """
    num_guesses = 0
    start = time.time()
    secret_number = generate_secret_number()

    while True:
        user_input = input_function(">>> ") 
        validation_error = validate_input(user_input)
        
        if validation_error:
            output_function(validation_error)
            continue

        num_guesses += 1

        bulls, cows = compare_numbers(secret_number, user_input)

        if bulls == 4:
            end = time.time()
            elapsed_time = end - start
            victory_message = f"""
                >>> {user_input}
                Correct, you've guessed the right number
                in {num_guesses} guesses!
                {SEPARATOR}
                That's amazing!
                The game took {format_time(elapsed_time)}
            """
            output_function(textwrap.dedent(victory_message))
            break        
        else:
            output_function(f">>> {user_input}\n"
                  f"{bulls} bull{'s' if bulls != 1 else ''}, "
                  f"{cows} cow{'s' if cows != 1 else ''}\n")
            output_function(SEPARATOR)     
    return num_guesses   


def main(input_function=input, output_function=print):
    """
    Main loop of the game. Handles multiple rounds and final statistics.
    """
    output_function(textwrap.dedent(f"""
    Hi there!
    {SEPARATOR}
    I've generated a random 4-digit number for you.
    Let's play a Bulls and Cows game.
    {SEPARATOR}
    Enter a number:"""))

    statistics = []

    while True:
        guesses = play_game(input_function=input_function, output_function=output_function)
        statistics.append(guesses)

        play_again = input_function("Do you want to play again? (yes): ")
        if play_again.lower() != "yes":
            break

    # Show summary
    output_function("\n" + SEPARATOR + "\nGame statistics:\n" + SEPARATOR)
    for i, guesses in enumerate(statistics, 1):
        output_function(f"Game {i:>2}: {guesses} guesses")
    output_function(SEPARATOR)
    output_function(f"Best result : {min(statistics)} attempts")
    output_function(
        f"Average     : {sum(statistics) / len(statistics):.2f} attempts"
        )


if __name__ == "__main__":
    main()
