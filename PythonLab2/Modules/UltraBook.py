from PythonLab2.Modules.AbstractLaptop import AbstractLaptop


class UltraBook(AbstractLaptop):
    def __init__(self, model, ram, screen_size, battery_life, weight, thickness):
        super().__init__(model, ram, screen_size)
        self.weight = weight
        self.thickness = thickness
        self.battery_life = battery_life

    def replace_battery(self, battery_life):
        print(f"In UltraBook you can't replace battery life")

    def __str__(self):
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}" \
               f"\nBattery life: {self.battery_life}\n" \
               f"Weight: {self.weight}\n" \
               f"Thickness: {self.thickness}\n"
