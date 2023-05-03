import random

def guess_the_number(difficulty_level):
    if difficulty_level == 1:
        easy_mode()
    elif difficulty_level == 2:
        intermediate_mode()
    elif difficulty_level == 3:
        advanced_mode()
    else:
        print("Invalid difficulty level")

def easy_mode():
    target = random.randint(1, 10)
    for i in range(3):
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == target:
            print("Correct! You've won the game.")
            return
    print(f"Sorry, you didn't guess the number. The number was {target}.")

def intermediate_mode():
    target = random.randint(1, 100)
    for i in range(10):
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == target:
            print("Correct! You've won the game.")
            return
        elif guess < target:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    print(f"Sorry, you didn't guess the number. The number was {target}.")

def advanced_mode():
    target = random.randint(1, 1000)
    for i in range(15):
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
            if guess == target:
                print("Correct! You've won the game.")
                return
            elif guess < target:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print(f"Sorry, you didn't guess the number. The number was {target}.")


def main():
    # You can change the difficulty level (1, 2, or 3) to demonstrate different topics
    difficulty_level = 1
    guess_the_number(difficulty_level)

if __name__ == "__main__":
    main()
