import random

# Prepare the deck of cards by creating pairs of cards and shuffling them
def prepare_deck():
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F'] # Create pairs of cards
    random.shuffle(cards) # Shuffle cards
    return cards

# Print the current state of the board
def print_board(cards, correct_guesses, previous_guesses=None):
    print("\nBoard:")
    for i, card in enumerate(cards):
        if i in correct_guesses: # If the card has been correctly guessed before, print it
            print("[%s]" % card, end=" ")
        elif previous_guesses and i in previous_guesses: # If the card was part of the previous guess, print it
            print("(%s)" % card, end=" ")
        else: # Else print an empty slot
            print("[ ]", end=" ")
        if ((i + 1) % 4 == 0): # Add a new line every 4 cards for better visibility
            print()

# Accept a guess from the player, validating that it's a number between 0 and 11 and hasn't been guessed before
def guess_card(correct_guesses):
    while True:
        try:
            # Accept input from the player
            guess = input("\nEnter the index of your guessed card (0-11), (R to restart the game): ")
            if guess.lower() == 'r': # If the player wants to restart the game, return 'r'
                return guess.lower()
            guess = int(guess) # Convert the guess to an integer
            # If the guess is not within 0 and 11, or it has been guessed correctly before, raise a ValueError
            if guess < 0 or guess > 11 or guess in correct_guesses:
                raise ValueError
            return guess
        except ValueError:
            print("Oops! Invalid index. Try again...")

# Let the player guess a pair of cards
def guess_pair(cards, correct_guesses):
    print_board(cards, correct_guesses)
    guess1 = guess_card(correct_guesses)

    if guess1 == 'r': # If the player wants to restart the game, return 'r'
        return guess1

    print_board(cards, correct_guesses, [guess1])
    guess2 = guess_card(correct_guesses)

    if guess2 == 'r': # If the player wants to restart the game, return 'r'
        return guess2

    print_board(cards, correct_guesses, [guess1, guess2])

    # If the player guessed a pair correctly, add both guesses to correct_guesses
    if cards[guess1] == cards[guess2]:
        print("\nYou've found a pair!")
        correct_guesses += [guess1, guess2]
    else:
        print("\nNo pair :(\n")

    return correct_guesses

# The main game logic
def play_game():
    print("\nWelcome to memory game!\n")
    correct_guesses = []
    cards = prepare_deck()
    # Let the player guess pairs until all pairs have been found
    while len(correct_guesses) < len(cards):
        result = guess_pair(cards, correct_guesses)
        if result == 'r': # If the player wants to restart the game, return 'r'
            return 'r'
        correct_guesses = result

    print("\nCongratulations! you won the game!") # Congratulate the player for winning the game

# Start the game, and allow the player to play again or quit after a game ends
def start_game():
    while True:
        play_again = play_game()
        if play_again != 'r': # If the player does not want to restart the game
            play_again = input("\nPress any key to play again, or 'Q' to quit the game: ").lower()
            if play_again == 'q': # If the player wants to quit the game, exit the loop
                break

if __name__ == '__main__':
    start_game() # Start the game when the script is run
