"""
Imports the AbstractLaptop class from the abstract_laptop module.
"""
from Modules.abstract_laptop import AbstractLaptop


class BussinesLaptop(AbstractLaptop):
    """
    Represents a business laptop, a type of laptop specifically designed for professional use.

    Attributes:
        model (str): The model name of the business laptop.
        ram (int): The amount of RAM in gigabytes (GB) in the laptop.
        screen_size (float): The size of the laptop screen in inches.
        battery_life (int): The battery life of the laptop in hours.
        version_of_windows (str): The version of Windows operating system installed on the laptop.
        licension_for_microsoft_office (str): The license type for Microsoft Office on the laptop.

    Methods:
        replace_battery(battery_life): Overrides the method
        from the AbstractLaptop class to indicate
        that battery replacement is not allowed for business laptops.
        __str__(): Returns a string representation of the business laptop.
    """

    # pylint:disable=too-many-arguments
    def __init__(self, model, ram, screen_size, battery_life, version_of_windows,
                 licension_for_microsoft_office):
        """
        Initializes a BussinesLaptop instance with the provided attributes.

        Args:
            model (str): The model name of the business laptop.
            ram (int): The amount of RAM in gigabytes (GB) in the laptop.
            screen_size (float): The size of the laptop screen in inches.
            battery_life (int): The battery life of the laptop in hours.
            version_of_windows (str): The version of Windows operating
            system installed on the laptop.
            licension_for_microsoft_office (str): The license type for Microsoft Office
            on the laptop.
        """
        super().__init__(model, ram, screen_size)
        self.version_of_windows = version_of_windows
        self.licension_for_microsoft_office = licension_for_microsoft_office
        self.battery_life = battery_life
        self.the_best_operation_system_set = "Windows 10 Ultimate", "Windows for business"

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
        Returns a string representation of the business laptop.

        Returns:
            str: A string representation of the business laptop.
        """
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}" \
               f"\nBattery life: {self.battery_life}\n"
