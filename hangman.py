import random

# List of 5 predefined words
words = ["python", "apple", "computer", "school", "coding"]

# Select a random word
word = random.choice(words)

# Initialize variables
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts left:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
else:
    print("\nGame Over!")
    print("The correct word was:", word)
