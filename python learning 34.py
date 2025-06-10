import random

low = 1
high = 100
answer = random.randint(low, high)
guesses = 0
is_running = True

print("Welcome to Python number guessing game...")
print(f"Select a number between {low} to {high}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high:
            print("The number is out of range.")
            print(f"Please select a number between {low} to {high}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {low} to {high}")
