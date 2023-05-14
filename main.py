class Laptop:
    instance = None
    charge = 0
    def __init__(self, model="", ram=0, screen_size=0, storage=0, battery_life=0):
        self.model = model
        self.ram = ram
        self.screen_size = screen_size
        self.storage = storage
        self.battery_life = battery_life

    def add_ram(self, add_this_ram):
        self.ram += add_this_ram
        print(add_this_ram, "GB of ram added")
    def add_storage(self, add_this_storage):
        self.storage += add_this_storage
        print(add_this_storage, "GB of storage added")
    def charge(self, max_level_of_charge):
        self.charge = max_level_of_charge
        print("Battery charged to", max_level_of_charge)

    @staticmethod
    def getInstance():
        if not Laptop.instance:
            Laptop.instance = Laptop("", 0, 0, 0, 0)
            return Laptop.instance


if __name__ == '__main__':

    laptops = [None] * 4
    laptops[0] = Laptop()
    laptops[1] = Laptop("Asus", 16, 17.3, 512, 8)
    laptops[2] = Laptop.getInstance()
    laptops[3] = Laptop.getInstance()
    for i in laptops:
        print(i.__dict__)
