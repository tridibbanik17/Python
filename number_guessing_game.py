# Guess a number between 1 and 20
# Say if the answer is higher or lower than their guess
# Give the user 3 tried to get it right

from random import randint

def play(number_of_tries):
    answer = randint(1, 20)


    for i in range(number_of_tries):
        number_of_guess_left = number_of_tries - i
        guess = int(input("Guess a number between 1 and 20: "))
        if (answer > guess):
            number_of_guess_left = number_of_guess_left - 1
            print(f"The answer is higher. You have {number_of_guess_left} more guess left.")
        elif (answer < guess):
            number_of_guess_left = number_of_guess_left - 1
            print(f"The answer is lower. You have {number_of_guess_left} more guess left.")
        else:
            print("You guessed it right!")
            return

    print(f"Sorry, you've used all your tries. The correct answer was {answer}.")

play(3)
