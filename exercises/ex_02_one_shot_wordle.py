""""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730463846"

secret_word: str = "python"
guess: str = input(f"What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
word_index: int = 0
result_emoji: str = ""
chr_in_word: bool = False
letter_index: int = 0

while int(len(guess)) != 6: 
    guess = input(f"That was not six letters! Try again: ")


while word_index < int(len(secret_word)):
        if guess[word_index] == secret_word[word_index]:
            result_emoji = result_emoji + GREEN_BOX
        else: 
            while (chr_in_word == False) and (letter_index < int(len(secret_word))):
                if secret_word[letter_index] == guess[word_index]:
                    chr_in_word = True
                letter_index = letter_index + 1
            if chr_in_word == True:
                result_emoji = result_emoji + YELLOW_BOX
            if chr_in_word == False:
                result_emoji = result_emoji + WHITE_BOX
        word_index = word_index + 1
        letter_index = 0
        chr_in_word = False
print(result_emoji)
if len(guess) == 6 and guess == secret_word:
    print(f"Woo! You got it!")
if len(guess) ==6 and guess != secret_word:
    print(f"Not quite. Play again soon!")
