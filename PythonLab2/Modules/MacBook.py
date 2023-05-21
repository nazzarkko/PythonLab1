from PythonLab2.Modules.AbstractLaptop import AbstractLaptop


class MacBook(AbstractLaptop):
    def __init__(self, model, ram, screen_size, battery_life, model_of_processor, version_of_ios):
        super().__init__(model, ram, screen_size)
        self.battery_life = battery_life
        self.model_of_processor = model_of_processor
        self.version_of_ios = version_of_ios

    def replace_battery(self, battery_life):
        self.battery_life = battery_life
        print(f"New battery life: {self.battery_life}")

    def __str__(self):
        return f"Model: {self.model}\nRAM: {self.ram}\nScreen size: {self.screen_size}\n" \
               f"Battery life: {self.battery_life}\n" \
               f"Model of processor: {self.model_of_processor}\n" \
               f"Version of IOS: {self.version_of_ios}\n "
