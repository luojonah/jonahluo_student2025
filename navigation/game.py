import random

# ---- Procedure with name, parameters, return type, and algorithm ----
def check_guess(word, guesses):
    """
    Checks which letters from the word have been guessed.

    Parameters:
        word (str): The hidden word.
        guesses (list): Letters the player has guessed.

    Returns:
        str: A string showing the word with correctly guessed letters and underscores.
    """
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


# ---- Read words from file (input from a file) ----
def load_words(words):
    """
    Loads a list of words from a text file.

    Parameters:
        filename (str): Name of the file containing words.

    Returns:
        list: A list of words from the file.
    """
    with open(words, "r") as file:
        words = file.read().splitlines()
    return words


# ---- Main Game Logic ----
def play_game():
    word_list = load_words("navigation/words.txt")  # Update path as needed

    while True:
        print("Welcome to 'Guess the Word'!")
        word = random.choice(word_list).lower()

        guessed_letters = []
        attempts = 6

        while attempts > 0:
            print("\nWord:", check_guess(word, guessed_letters))
            print("Guessed letters:", guessed_letters)
            guess = input("Enter a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in word:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
            else:
                print("Good guess!")

            if all(letter in guessed_letters for letter in word):
                print("\n🎉 Congratulations! You guessed the word:", word)
                break
        else:
            print("\n😢 Out of attempts! The word was:", word)

        # Ask if user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()
