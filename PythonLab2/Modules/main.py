"""
Create a collection of laptops and perform operations on it.
"""
from PythonLab2.Modules.gaming_laptop import GamingLaptop
from PythonLab2.Modules.bussines_laptop import BussinesLaptop
from PythonLab2.Modules.mac_book import MacBook
from PythonLab2.Modules.ultra_book import UltraBook
from PythonLab2.Manager.laptop_manager import LaptopManager

if __name__ == '__main__':
    laptops = LaptopManager()
    """
    Create an instance of LaptopManager to manage a collection of laptops.
    """

    laptops.add_laptop(GamingLaptop("Asus", 16, 15.6, 6, "Nvidia", 2))
    laptops.add_laptop(BussinesLaptop("Lenovo", 8, 14, 8, "Windows 10 Home", "True"))
    laptops.add_laptop(MacBook("MacBook", 8, 13, 10, "M1", "MacOS"))
    laptops.add_laptop(UltraBook("HP", 8, 13, 10, 1.5, 1))
    laptops.add_laptop(GamingLaptop("Dell", 32, 16.2, 6, "GTX", 4))

    laptops[0].replace_battery(1)

