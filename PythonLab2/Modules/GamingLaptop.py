from PythonLab2.Modules.AbstractLaptop import AbstractLaptop


class GamingLaptop(AbstractLaptop):
    def __init__(self, model, ram, screen_size, battery_life, graphics_card, count_of_ventilators):
        super().__init__(model, ram, screen_size)
        self.graphics_card = graphics_card
        self.count_of_ventilators = count_of_ventilators
        self.battery_life = battery_life

    def replace_battery(self, battery_life):
        self.battery_life = battery_life
        print(f"New battery life: {self.battery_life}")

    def __str__(self):
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}" \
               f"\nBattery life: {self.battery_life}\nGraphics card: {self.graphics_card}" \
                 f"\nCount of ventilators: {self.count_of_ventilators}\n"
