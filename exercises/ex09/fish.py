"""File to define Fish class."""
__author__ = "730463846"


class Fish:
    """Defines attributes and methods for class fish."""
    age: int

    def __init__(self):
        """Initializes fish's age to 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Ages the fish each day in the river."""
        self.age += 1
        return None