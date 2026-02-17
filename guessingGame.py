import random
import time

def main():
    secret_number = random.randint(1, 10)
    game(secret_number)

def game(answer):
    while True:
        try:
            guess = int(input("\nGuess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                raise ValueError

            elif guess > answer:
                print("The answer is lower than ", guess)
                time.sleep(1)
                continue

            elif guess < answer:
                print("The answer is higher than ", guess)
                time.sleep(1)
                continue

            else:
                print("Correct! You Win!")
                break

        except ValueError:
            print("Please enter an Integer between 1 and 10.")
            time.sleep(1)

main()