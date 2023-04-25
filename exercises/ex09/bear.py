"""File to define Bear class."""
__author__ = "730463846"


class Bear:
    """Defines Bear class."""
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes attributes to 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Ages bear and adds hunger score each day."""
        self.hunger_score -= 1
        self.age += 1
        return None

    def eat(self, num_fish: int):
        """Increases hunger score when the bear eats."""
        self.hunger_score += num_fish
        return None