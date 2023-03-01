"""EX03 - Wordle!"""
__author__ = "730463846"

def contains_char(word: str, char: str) -> bool:
    """Determines whether a given character is found in a word"""
    assert len(char) == 1
    char_index = 0
    while char_index < len(word): 
        if word[char_index] == char:
           return True
        else: 
            char_index = char_index + 1
    return False

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    char_index = 0
    result_emoji = ""
    while char_index < len(guess):
        if guess[char_index] == secret[char_index]:
            result_emoji = result_emoji + GREEN_BOX
        else: 
            if contains_char(secret, guess[char_index]) == True: 
                result_emoji = result_emoji + YELLOW_BOX
            else:
                result_emoji = result_emoji + WHITE_BOX
        char_index= char_index + 1
    return result_emoji
def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length: 
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    n_turns = 1
    success: bool = False
    while n_turns <= 6 and not success: 
        print(f"=== Turn {n_turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret: 
            success = True
            print(f"You won in {n_turns}/6 turns!")
        n_turns = n_turns + 1
    if n_turns >= 7: 
        print("X/6 - Sorry, try again tomorrow!")
if __name__ == "__main__":
    main()