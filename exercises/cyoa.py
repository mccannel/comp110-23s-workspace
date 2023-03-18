"""Choose your own adventure!"""
__author__ = "730463845"

player: str = ""
points: int = 0
possible_points: int = 0
CAT: str = "\U0001F408"
DOG: str = "\U0001F436"
UNICORN: str = "\U0001F984"


def main() -> None: 
    greet()
    idx: int = 0
    while idx == 0: 
        global points
        global possible_points
        adoption: str = input("Would you like to adopt a pet? (Enter Yes or No): ")
        if adoption == "Yes": 
            print(f"Which pet would you like to adopt 1) {CAT} , 2) {DOG}, or 3) {UNICORN}?")
            pet: int = input("Choose a pet by typing 1, 2, or 3: ")
            if pet == "1":
                cat_game() 
                possible_points += 3
            if pet == "2": 
                points = dog_game(points)
                possible_points += 4
            if pet == "3": 
                points = unicorn_game(points)
                possible_points += 3
        if adoption == "No":
            idx -= 1
        if points < 0: 
            points == 0
        print(f"You have earned {points} points.")
    print(f"Goodbye {player}, I hope you enjoyed Pet World!")
    if points / possible_points >= 0.5: 
        print("You are a good pet owner!")
    if points / possible_points < 0.5: 
        print("You weren't a good pet owner:(")

def greet() -> None: 
    print("Welcome to Pet World! Adopt your own virtual pet and take care of it!")
    global player
    player = input("What is your name?: ")


def cat_game() -> None: 
    print(f"Here is your new pet {CAT}")
    pet_name: str = input(f"{player}, What do you want to name your pet?: ")
    food: str = input (f"{pet_name} is hungry. Do you want to feed your cat? (Enter Yes or No): ")
    if food == "Yes": 
        global points
        points += 1
    else:
        points -= 1
    play: str = input ("Do you want to play with your cat? (Enter Yes or No): ")
    if play == "Yes": 
        points += 1 
    else:
        points -= 1
    water: str = input (f"{pet_name} is thirsty. Do you want give your cat water? (Enter Yes or No): ")
    if water == "Yes": 
        points += 1
    else:
        points -= 1
    import random
    if random.randint(0,1) == 1: 
        print (f"{pet_name} isn't feeling well") 
        vet: str = input("Do you want to take your cat to the vet? (Enter Yes or No): ")
        if vet == "Yes": 
            points += 1
            print("{pet_name} is feeling much better now")
        else:
            points -= 1
    


def dog_game(points: int) -> int:
    print(f"Here is your new pet {DOG}")
    pet_name: str = input(f"{player}, What do you want to name your dog?: ")
    walk: str = input("Do you want to walk your dog? (Enter Yes or No): ")
    if walk == "Yes":
        points += 1 
    else:
        points -= 1
    food: str = input("Do you want to feed your dog? (Enter Yes or No): ")
    if food == "Yes": 
        points += 1
    else:
        points -= 1
    water: str = input(f"{pet_name} is thirsty. Do you want to give your dog water? (Enter Yes or No): ")
    if water == "Yes": 
        points += 1
    else:
        points -= 1
    play: str = input ("Do you want to play with your dog? (Enter Yes or No): ")
    if play == "Yes":
        points += 1
    else:
        points -= 1
    return points


def unicorn_game(points: int) -> int:
    print(f"Here is your new pet {UNICORN}")
    pet_name: str = input(f"{player}, What do you want to name your unicorn?: ")
    import random 
    if random.randint(0,1) == 0:
        print("Your unicorn is a special breed that has wings and can fly!")
        print("This means you need to take special care of your unicorn and fly it regularly")
        fly: str = input("Do you want to fly your unicorn? (Enter Yes or No): ")
        if fly == "Yes": 
            points += 1
    food: str = input("Do you want to feed your unicorn? (Enter Yes or No): " )
    if food == "Yes":
        points += 1
    else:
        points -= 1
    water: str = input("Do you want to give your unicorn water? (Enter Yes or No): ")
    if water == "Yes": 
        points += 1
    else:
        points -= 1
    print("Your unicorn's mane needs to be brushed regularly.")
    brush: str = input(f"Do you want to brush {pet_name}'s hair? (Enter Yes or No): ")
    if brush == "Yes": 
        points += 1
    else:
        points -= 1
    return points

if __name__ == "__main__":
  main()