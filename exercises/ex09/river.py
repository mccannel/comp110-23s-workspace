"""File to define River class."""
__author__ = "730463846"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """Defines attributes and methods for class River."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def bears_eating(self):
        """When bears eat, fish are removed and bear's hunger score increases."""
        for bear in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """If Bears are too hungery, they starve."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def check_ages(self):
        """Bears and fish are removed as they age."""
        new_fish: list[Fish] = []
        for fish in self.fish: 
            if fish.age <= 3:
                new_fish.append(Fish())
        self.fish = new_fish
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(Bear())
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """New fish are added as they reproduce."""
        for fish in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """New bears are added to the river as they reproduce."""
        for bear in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    def remove_fish(self, amount: int):
        """Fish are removed."""
        for item in range(amount):
            self.fish.pop(item)
        return None

    def view_river(self):
        """Gives status updates each day of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Describes what happens on each day on the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Calls a new river day 7 times, simulating 1 week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()