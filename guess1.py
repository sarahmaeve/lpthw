# inspired by https://www.youtube.com/watch?v=O17TzRU0Pss
# but with a function.
# this can be improved a lot.

import random

def analyze_guess(guess, target):
    guess = int(guess)
    if not type(guess) == 'int':
        msg = "I don't understand that."
    if guess < target:
        msg = "Too low!"
    elif guess > target:
        msg = "Too high!"
    elif guess == target:
        msg = "Correct! You win!"
    else:
        msg = "Huh?"
    return msg

name = input("Hello, what is your name? ")
if not name:
    name = 'Nemo'
print(f"{name}, I am thinking of a number between one and ten.")
number = random.randint(1,10)
guesses = 0
while guesses < 3:
    print(f"What is your guess, {name}?")
    user_guess = input("> ")
    analysis = analyze_guess(user_guess, number)
    print(analysis)
    if analysis == "Correct! You win!":
        break
    else:
        guesses += 1
else:
    print(f"Aww, out of guesses. I win! I was thinking of {number}.")
