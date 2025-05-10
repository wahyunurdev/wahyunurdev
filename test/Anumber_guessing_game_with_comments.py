import random

# Function to print colored text
def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Welcome message
print(colored_text("🎯 Welcome to the Number Guessing Game!", "1;32"))
print(colored_text("The system will randomly choose a number between 1 and 100. You have 10 chances to guess it.", "1;34"))

# Main game loop
while True:
    # Set up initial variables
    target = random.randint(1, 100)   # Random number to guess
    guesses = []                      # A list to keep track of guessed numbers
    max_attempts = 10                 # Maximum number of guesses allowed
    attempt = 0                       # Current number of attempts

    # Start the guessing loop
    while attempt < max_attempts:
        # Ask user for input
        guess = input(colored_text(f"\nAttempt {attempt + 1}, enter a number (1~100): ", "1;36"))

        # Check if input is a number
        if not guess.isdigit():
            print(colored_text("⚠️ Please enter a valid integer!", "1;31"))
            continue  # Skip the rest of the loop and ask again

        # Convert input to an integer
        guess = int(guess)

        # Check if the guess is within valid range
        if guess < 1 or guess > 100:
            print(colored_text("❌ Number out of range! Please enter a number between 1 and 100.", "1;31"))
            continue  # Skip the rest of the loop and ask again

        # Check if the number has already been guessed
        if guess in guesses:
            print(colored_text("🔁 You've already guessed this number!", "1;33"))
            continue  # Skip the rest of the loop and ask again
        else:
            guesses.append(guess)  # Add the guess to the list
            attempt += 1           # Increase the attempt count

        # Compare guess with the target number
        if guess == target:
            print(colored_text(f"🎉 Congratulations! You guessed it right. The answer was {target}", "1;32"))
            break  # Exit the loop because the guess is correct
        elif guess < target:
            print(colored_text("📉 Too low!", "1;33"))  # Hint: guess is too small
        else:
            print(colored_text("📈 Too high!", "1;33"))  # Hint: guess is too big

    # If all attempts are used and no correct guess
    if attempt == max_attempts and guess != target:
        print(colored_text(f"\n😢 Sorry, the correct answer was {target}. Better luck next time!", "1;31"))

    # Show all guesses made by the user
    print(colored_text(f"\nYour guesses: {guesses}", "1;34"))

    # Ask if the user wants to play again
    play_again = input(colored_text("\nDo you want to play again? (yes/no): ", "1;36")).strip().lower()
    if play_again != 'yes':
        print(colored_text("👋 Thanks for playing! Goodbye!", "1;32"))
        break