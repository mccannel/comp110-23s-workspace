"""EX01 - Chardle - A cute step toward Wordle"""
__author__ = "730463845"

word: str = input("Enter a 5-character word: ")
if (len(word) > 5):
    print("Error: Word must contain 5 characters")
    exit()
if (len(word) < 5):
    print("Error: Word must contain 5 characters")
    exit()
char: str = input("Enter a single character: ")
if (len(char) > 1):
    print("Error: Character must be a single character.")
    exit()
if (len(char) < 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + char, "in", word)
total: int = 0
if (word [0] == char):
    print(char + " found at index 0")
    total = total + 1 
if (word [1] == char):
    print (char + " found at index 1")
    total = total + 1
if (word [2] == char):
    print (char + " found at index 2")
    total = total + 1 
if (word [3] == char):
    print (char + " found at index 3")
    total = total + 1
if (word [4] == char):
    print (char + " found at index 4")
    total = total + 1

if (total > 0):
    print(str(total) + " instances of " + char, "found in " + word)

else: 
    print("No instances of " + char, "found in " + word)


