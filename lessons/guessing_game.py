"""Asks user for a number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing: 
    if guess ==SECRET:
        print("Yay! You got it right.")
        playing = False
    else: 
        print("wrong number:(")
        guess= int(input ("Make another guess"))