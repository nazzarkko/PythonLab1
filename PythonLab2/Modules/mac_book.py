"""
Import the AbstractLaptop class from the abstract_laptop module.
"""
from PythonLab2.Modules.abstract_laptop import AbstractLaptop
from PythonLab2.Decorator.logged_decorator import logged_decorator
from PythonLab2.Exception.not_usable_battery_exception import NotUsableBattery


class MacBook(AbstractLaptop):
    """
    Represents a MacBook, a type of laptop produced by Apple.

    Attributes:
        model (str): The model name of the MacBook.
        ram (int): The amount of RAM in gigabytes (GB) in the MacBook.
        screen_size (float): The size of the MacBook screen in inches.
        battery_life (int): The battery life of the MacBook in hours.
        model_of_processor (str): The model of the processor in the MacBook.
        version_of_ios (str): The version of the iOS operating system installed on the MacBook.

    Methods:
        replace_battery(battery_life): Overrides the method from the AbstractLaptop class to replace
         the battery life of the MacBook.
        __str__(): Returns a string representation of the MacBook.
    """

    # pylint:disable=too-many-arguments
    def __init__(self, model, ram, screen_size, battery_life, model_of_processor, version_of_ios):
        """
        Initializes a MacBook instance with the provided attributes.

        Args:
            model (str): The model name of the MacBook.
            ram (int): The amount of RAM in gigabytes (GB) in the MacBook.
            screen_size (float): The size of the MacBook screen in inches.
            battery_life (int): The battery life of the MacBook in hours.
            model_of_processor (str): The model of the processor in the MacBook.
            version_of_ios (str): The version of the iOS operating system installed on the MacBook.
        """
        super().__init__(model, ram, screen_size)
        self.battery_life = battery_life
        self.model_of_processor = model_of_processor
        self.version_of_ios = version_of_ios
        self.the_best_operation_system_set = "macOS Big Sur", "macOS Monterey"

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
        Returns a string representation of the MacBook.

        Returns:
            str: A string representation of the MacBook.
        """
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}\n" \
               f"Battery life: {self.battery_life}\n" \
               f"Model of processor: {self.model_of_processor}\n" \
               f"Version of iOS: {self.version_of_ios}\n"
