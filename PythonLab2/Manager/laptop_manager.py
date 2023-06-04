""" Creating class LaptopManager. """


class LaptopManager:
    """
    A class that manages a collection of laptops.

    Attributes:
        laptops (list): A list to store the laptops in the collection.

    Methods:
        add_laptop(laptop): Adds a laptop to the collection.
        choose_laptop_with_ram(ram): Returns a list of laptops with the specified RAM size.
        find_laptop_with_more_screen_size(screen_size): Returns a list of laptops with
        a screen size greater
        than or equal to the specified value.
    """

    def __init__(self):
        """
        Initializes an empty list to store the laptops.
        """
        self.laptops = []

    def add_laptop(self, laptop):
        """
        Adds a laptop to the collection.

        Args:
            laptop: An instance of a laptop to be added.
        """
        self.laptops.append(laptop)

    def choose_laptop_with_ram(self, ram):
        """
        Returns a list of laptops with the specified RAM size.

        Args:
            ram (int): The RAM size in gigabytes (GB) to filter the laptops.

        Returns:
            list: A list of laptops with the specified RAM size.
        """
        return list(filter(lambda laptop: laptop.ram == ram, self.laptops))

    def find_laptop_with_more_screen_size(self, screen_size):
        """
        Returns a list of laptops with a screen size greater than or equal to the specified value.

        Args:
            screen_size (float): The minimum screen size in inches to filter the laptops.

        Returns:
            list: A list of laptops with a screen size greater than or equal to the specified value.
        """
        return list(filter(lambda laptop: laptop.screen_size >= screen_size, self.laptops))

    def __len__(self):
        return len(self.laptops)

    def __getitem__(self, item):
        return self.laptops[item]

    def __iter__(self):
        return iter(self.laptops)

    def laptop_with_index(self):
        for index, laptop in enumerate(self.laptops):
            print(f"{index}: {laptop}")

    def laptop_battery_list(self):
        return [laptop.laptop_battery_list for laptop in self.laptops]

    def zipper(self):
        for laptop, result in zip(self.laptops, self.laptop_battery_list()):
            print(f"Our {laptop}: has {result} ")

    def any_laptop_has_ram_more_than_choosen(self, choosen_ram):
        return any(laptop.ram >= choosen_ram for laptop in self.laptops)

    def all_laptop_has_ram_more_than_choosen(self, choosen_ram):
        return all(laptop.ram >= choosen_ram for laptop in self.laptops)
