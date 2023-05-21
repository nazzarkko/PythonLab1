class LaptopManager:
    def __init__(self):
        self.laptops = []

    def add_laptop(self, laptop):
        self.laptops.append(laptop)

    def choose_laptop_with_ram(self, ram):
        return [laptop for laptop in self.laptops if laptop.ram == ram]

    def find_laptop_with_more_screen_size(self, screen_size):
        return [laptop for laptop in self.laptops if laptop.screen_size >= screen_size]
