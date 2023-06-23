"""
Import the AbstractLaptop class from the abstract_laptop module.
"""
from Modules.abstract_laptop import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    """
    Represents a gaming laptop, a type of laptop designed for gaming enthusiasts.

    Attributes:
        model (str): The model name of the gaming laptop.
        ram (int): The amount of RAM in gigabytes (GB) in the gaming laptop.
        screen_size (float): The size of the gaming laptop screen in inches.
        battery_life (int): The battery life of the gaming laptop in hours.
        graphics_card (str): The graphics card installed in the gaming laptop.
        count_of_ventilators (int): The count of ventilators in the gaming laptop.

    Methods:
        replace_battery(battery_life): Overrides the method from the AbstractLaptop class to replace
         the battery life of the gaming laptop.
        __str__(): Returns a string representation of the gaming laptop.
    """

    # pylint:disable=too-many-arguments
    def __init__(self, model, ram, screen_size, battery_life, graphics_card, count_of_ventilators):
        """
        Initializes a GamingLaptop instance with the provided attributes.

        Args:
            model (str): The model name of the gaming laptop.
            ram (int): The amount of RAM in gigabytes (GB) in the gaming laptop.
            screen_size (float): The size of the gaming laptop screen in inches.
            battery_life (int): The battery life of the gaming laptop in hours.
            graphics_card (str): The graphics card installed in the gaming laptop.
            count_of_ventilators (int): The count of ventilators in the gaming laptop.
        """
        super().__init__(model, ram, screen_size)
        self.graphics_card = graphics_card
        self.count_of_ventilators = count_of_ventilators
        self.battery_life = battery_life
        self.the_best_operation_system_set = "Windows 10", "Windows 11"

    def replace_battery(self, battery_life):
        """
        Overrides the replace_battery method from the AbstractLaptop class.
        Prints a message indicating that battery replacement is not allowed for business laptops.

        Args:
            battery_life (int): The new battery life to set .
        """
        print(f"New battery life: {battery_life}")

    def __str__(self):
        """
        Returns a string representation of the gaming laptop.

        Returns:
            str: A string representation of the gaming laptop.
        """
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}" \
               f"\nBattery life: {self.battery_life}\nGraphics card: {self.graphics_card}" \
               f"\nCount of ventilators: {self.count_of_ventilators}\n"
