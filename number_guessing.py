import random

print("Welcome to Number Guessing Game!")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct! You guessed it in", attempts, "attempts.")
        break
