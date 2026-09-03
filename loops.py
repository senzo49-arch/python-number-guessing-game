print("######## GUESSING GAME IN PYTHON ######")

# The secret number the user has to guess
secret_number = 7

# Ask the user to enter their first guess
guess = int(input("Guess a number from 1 to 10: "))

# Keep asking until the user guesses the correct number
while guess != secret_number:

    # Check if the guess is lower than the secret number
    if guess < secret_number:
        print("Too low!")

    # If it is not lower, it must be higher
    else:
        print("Too high!")

    # Ask the user to try another number
    guess = int(input("Try again: "))

# This runs when the correct number is guessed
print("Correct! You won!")