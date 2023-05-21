from abc import ABC, abstractmethod


class AbstractLaptop(ABC):
    def __init__(self, model="", ram=0, screen_size=0, storage=0, battery_life=0):
        self.model = model
        self.ram = ram
        self.screen_size = screen_size
        self.storage = storage
        self.battery_life = battery_life

    @abstractmethod
    def replace_battery(self, battery_life):
        pass
