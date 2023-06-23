"""
Import the AbstractLaptop class from the abstract_laptop module.
"""
from PythonLab2.Modules.abstract_laptop import AbstractLaptop
from PythonLab2.Decorator.logged_decorator import logged_decorator
from PythonLab2.Exception.not_usable_battery_exception import NotUsableBattery


class UltraBook(AbstractLaptop):
    """
    A class representing an UltraBook, a type of laptop known for its lightweight and thin design.

    Attributes:
        model (str): The model name of the UltraBook.
        ram (int): The amount of RAM in gigabytes (GB) in the UltraBook.
        screen_size (float): The size of the UltraBook screen in inches.
        battery_life (int): The battery life of the UltraBook in hours.
        weight (float): The weight of the UltraBook in kilograms (kg).
        thickness (float): The thickness of the UltraBook in centimeters (cm).

    Methods:
        replace_battery(battery_life): Method to replace the battery life of the UltraBook.
        __str__(): Returns a string representation of the UltraBook.

    """

    # pylint:disable=too-many-arguments
    def __init__(self, model, ram, screen_size, battery_life, weight, thickness):
        """
        Initializes an UltraBook instance with the provided attributes.

        Args:
            model (str): The model name of the UltraBook.
            ram (int): The amount of RAM in gigabytes (GB) in the UltraBook.
            screen_size (float): The size of the UltraBook screen in inches.
            battery_life (int): The battery life of the UltraBook in hours.
            weight (float): The weight of the UltraBook in kilograms (kg).
            thickness (float): The thickness of the UltraBook in centimeters (cm).
        """
        super().__init__(model, ram, screen_size)
        self.weight = weight
        self.thickness = thickness
        self.battery_life = battery_life
        self.the_best_operation_system_set = "Windows 7 Home", "Windows 10 Home"

    @logged_decorator(NotUsableBattery, "file")
    def replace_battery(self, battery_life):
        """
        Overrides the replace_battery method from the AbstractLaptop class.
        Prints a message indicating that battery replacement is not allowed for business laptops.

        Args:
            battery_life (int): The new battery life to set .
        """
        print(f"New battery life: {battery_life}")
        if battery_life > 8 or battery_life < 2:
            raise NotUsableBattery
        return battery_life

    def __str__(self):
        """
        Returns a string representation of the UltraBook.

        Returns:
            str: String representation of the UltraBook.
        """
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}\n" \
               f"Battery life: {self.battery_life}\n" \
               f"Weight: {self.weight}\n" \
               f"Thickness: {self.thickness}\n"
