# ...existing code...
import random
import sys

def play_game(min_val=1, max_val=100):
    secret = random.randint(min_val, max_val)
    attempts = 0
    print(f"Guess a number between {min_val} and {max_val}. (type 'q' to quit)")

    while True:
        try:
            guess = input("Your guess: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            return

        if guess.lower() in ("q", "quit", "exit"):
            print("Goodbye.")
            return

        try:
            g = int(guess)
        except ValueError:
            print("Invalid input. Enter an integer.")
            continue

        attempts += 1
        if g == secret:
            print(f"Correct! The number was {secret}. Attempts: {attempts}")
            return
        elif g < secret:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


def main():
    print("NUMBER GUESSING GAME")
    while True:
        try:
            rng = input("Enter max number (default 100) or press Enter: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            return

        if rng == "":
            max_n = 100
        else:
            try:
                max_n = int(rng)
                if max_n < 1:
                    print("Please enter a positive integer.")
                    continue
            except ValueError:
                print("Invalid number. Try again.")
                continue

        play_game(1, max_n)

        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()
# ...existing code...