import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    tries = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            user_guess = int(input("41: "))
        except ValueError:
            print("That's not a valid number!")
            continue

        tries += 1

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You found the number in {tries} tries.")
            break

def play_again():
    while True:
        play = input("Do you want to play again? (yes/no): ").lower()
        if play == "yes":
            guess_number()
        elif play == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if "name" == "_main_":
    guess_number()
play_again()
