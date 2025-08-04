# Higher or Lower: Number Guessing Game v8
# By Jano
# Refactoring
from random import randint
from time import time

highscore_attempts: int = 0
highscore_time: float = 0


def start_up() -> str:
    # global highscore_attempts
    # global highscore_time
    difficulties: list = ['1', '2', '3']
    while True:
        print('\n'
              'Welcome to the Higher or Lower: Number Guessing Game!\n'
              "I'm thinking of a number between 1 and 100...")
        difficulty = (input('Please select the difficulty level:\n'
                            '\n'
                            '1.  Easy (10 guesses & 1 hint)\n'
                            '2.  Medium (5 guesses & 1 hint)\n'
                            '3.  Hard (3 guesses & 0 hints)\n'
                            'he. Help menu\n'
                            '\n'
                            'Enter your choice: '))
        if difficulty in difficulties:
            # print(f"{difficulty=}")
            return difficulty
            break
        elif difficulty.lower() == 'he':
            print('\n'
                  '(1)  Easy difficulty\n'
                  '(2)  Medium difficulty\n'
                  '(3)  Hard difficulty\n'
                  '(he) Help Menu\n'
                  '(hi) High Scores\n'
                  '(h)  Hint\n'
                  '(c)  Crash\n'
                  '(y)  Yes\n'
                  '(n)  No')
        elif difficulty.lower() == 'hi':
            print('\nHighscores:\n'
                  f'Fastest time:    {highscore_time}\n'
                  f'Lowest attempts: {highscore_attempts}')
        else:
            print('\n'
                  'Please enter a valid input!')
            continue


def set_up_1(difficulty) -> int:
    difficulties: dict = {
        '1': 'Easy',
        '2': 'Medium',
        '3': 'Hard'
    }
    if difficulty == '1':
        guesses = 10
    elif difficulty == '2':
        guesses = 5
    else:
        guesses = 3
    # print(f'{guesses=}')
    print('\n'
          f'Great! You have selected the {difficulties[difficulty]} difficulty level.\n'
          "Let's start the game!")
    return guesses


def set_up_2(difficulty) -> int:
    if difficulty == '1' or difficulty == '2':
        hints = 1
    else:
        hints = 0
    # print(f'{hints=}')
    return hints


def set_up_3() -> int:
    secret_number: int = randint(1, 100)
    # print(f'{secret_number=}')
    return secret_number


def hint(hints: int, secret_number: int) -> int:
    if hints != 0:
        hints -= 1
        random_high: int = secret_number + randint(5, 15)
        random_low: int = secret_number - randint(5, 15)
        print(
            f'The secret number is inbetween {random_low} and {random_high}.')
    else:
        print('You are all out of hints!')
    return hints


def find_highscore(current_score, highscore):
    highscore = current_score
    if type(highscore) == int:
        score_type = ['attempts', 'attempts']
    else:
        score_type = ['time', 'seconds']
    print(
        f'New Highscore! You got a highscore in {score_type[0]}, only needing {highscore} {score_type[1]}.')
    return highscore


def playing(guesses: int, hints: int, secret_number: int):
    attempts: int = 0
    start: float = time()
    global highscore_attempts
    global highscore_time
    while True:
        if guesses == 0:
            retry: str = input(
                '\nYou ran out of guesses! Would you like to continue this game? (y/n): ')
            if retry.lower() == 'y':
                guesses = -1
                continue
            elif retry.lower() == 'n':
                break
        else:
            # try:
            # print(f'{guesses=}')
            # print(f'{hints=}')
            user_guess = (input('\nEnter your guess: '))
            if user_guess.lower() == 'h':
                hints = hint(hints, secret_number)
            elif user_guess.lower() == 'c':
                break
            elif 0 <= int(user_guess) <= 100:
                attempts += 1
                guesses -= 1
                if int(user_guess) > secret_number:
                    print(
                        f'Incorrect! The number is less than {user_guess}.')
                elif int(user_guess) < secret_number:
                    print(
                        f'Incorrect! The number is greater than {user_guess}.')
                else:
                    end: float = time()
                    total_time = end - start
                    print(
                        f'Congratulations! You guessed the correct number in {attempts} attempts.\n'
                        f'It also took you {round(total_time, 5)} seconds!')
                    # print(f'{attempts=}')
                    # print(f'{highscore_attempts=}')
                    if attempts < highscore_attempts or highscore_attempts == 0:
                        highscore_attempts = find_highscore(
                            attempts, highscore_attempts)  # type: ignore
                    if total_time < highscore_time or highscore_time == 0:
                        highscore_time = find_highscore(
                            total_time, highscore_time)  # type: ignore
                    break
            # except:
           # print('Invalid Input')


def play_game():
    while True:
        difficulty = start_up()
        guesses = set_up_1(difficulty)
        hints = set_up_2(difficulty)
        secret_number = set_up_3()
        playing(guesses, hints, secret_number)

        play_again: str = input('\nWould you like to play again? (y/n): ')
        if play_again.lower() == 'n':
            print('\nThanks for playing!\n')
            break


play_game()
