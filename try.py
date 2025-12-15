import random

def start_game():
    print("\n--- Codespace Number Guesser ---")
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I have picked a number between 1 and 100.")
    print("Type your guess and hit Enter.\n")

    while True:
        try:
            # Taking input from the user
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret_number:
                print(" -> Too low! Try again.")
            elif guess > secret_number:
                print(" -> Too high! Try again.")
            else:
                print(f"\nSUCCESS! You found the number {secret_number} in {attempts} tries.")
                print("Your Codespace is working perfectly.")
                break
        except ValueError:
            print(" -> Please enter a valid integer.")

if __name__ == "__main__":
    start_game()