
import random

# Print welcome message
print("🎯 Welcome to the Number Guessing Game!")
print("The system will randomly choose a number between 1 and 100. You have 10 chances to guess it.")

# Set up initial variables
target = random.randint(1, 100)   # Random number to guess
guesses = []                      # A list to keep track of guessed numbers
max_attempts = 10                 # Maximum number of guesses allowed
attempt = 0                       # Current number of attempts

# Start the guessing loop
while attempt < max_attempts:
    # Ask user for input
    guess = input(f"\nAttempt {attempt + 1}, enter a number (1~100): ")

    # Check if input is a number
    if not guess.isdigit():
        print("⚠️ Please enter a valid integer!")
        continue  # Skip the rest of the loop and ask again

    # Convert input to an integer
    guess = int(guess)

    # Check if the guess is within valid range
    if guess < 1 or guess > 100:
        print("❌ Number out of range! Please enter a number between 1 and 100.")
        continue  # Skip the rest of the loop and ask again

    # Check if the number has already been guessed
    if guess in guesses:
        print("🔁 You've already guessed this number!")
        pass  # Do nothing, just a placeholder
    else:
        guesses.append(guess)  # Add the guess to the list
        attempt += 1           # Increase the attempt count

    # Compare guess with the target number
    if guess == target:
        print(f"🎉 Congratulations! You guessed it right. The answer was {target}")
        break  # Exit the loop because the guess is correct
    elif guess < target:
        print(""
              " Too low!")  # Hint: guess is too small
    else:
        print("📈 Too high!")  # Hint: guess is too big

# If all attempts are used and no correct guess
if attempt == max_attempts and guess != target:
    print(f"\n😢 Sorry, the correct answer was {target}. Better luck next time!")

# Show all guesses made by the user
print(f"\nYour guesses: {guesses}")
