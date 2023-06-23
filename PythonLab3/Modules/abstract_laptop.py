"""
Import from the abc module the ABC class and the abstractmethod decorator.
"""
from abc import ABC, abstractmethod


# pylint: disable= too-few-public-methods
class AbstractLaptop(ABC):
    """
    An abstract base class representing a laptop.

    Attributes:
        model (str): The model name of the laptop.
        ram (int): The amount of RAM in gigabytes (GB) in the laptop.
        screen_size (float): The size of the laptop screen in inches.
        storage (int): The storage capacity of the laptop in gigabytes (GB).
        battery_life (int): The battery life of the laptop in hours.

    Methods:
        replace_battery(battery_life): Abstract method to replace the battery life of the laptop.
    """

    # pylint:disable=too-many-arguments
    def __init__(self, model="", ram=0, screen_size=0, storage=0, battery_life=0):
        """
        Initializes an AbstractLaptop instance with the provided attributes.

        Args:
            model (str): The model name of the laptop.
            ram (int): The amount of RAM in gigabytes (GB) in the laptop.
            screen_size (float): The size of the laptop screen in inches.
            storage (int): The storage capacity of the laptop in gigabytes (GB).
            battery_life (int): The battery life of the laptop in hours.
        """
        self.model = model
        self.ram = ram
        self.screen_size = screen_size
        self.storage = storage
        self.battery_life = battery_life
        self.the_best_operation_system_set = set()

    @abstractmethod
    def replace_battery(self, battery_life):
        """
        Abstract method to replace the battery life of the laptop.
        Args:
        battery_life (int): The new battery life to set for the laptop.
        """


def __iter__(self):
    return iter(self.the_best_operation_system_set)
