from PythonLab2.Modules.GamingLaptop import GamingLaptop
from PythonLab2.Modules.BussinesLaptop import BussinesLaptop
from PythonLab2.Modules.MacBook import MacBook
from PythonLab2.Modules.UltraBook import UltraBook
from PythonLab2.Manager.LaptopManager import LaptopManager

if __name__ == '__main__':
    laptops = LaptopManager()
    laptops.add_laptop(GamingLaptop("Asus", 16, 15.6, 6, "Nvidia", 2))
    laptops.add_laptop(BussinesLaptop("Lenovo", 8, 14, 8, 1.5, 1))
    laptops.add_laptop(MacBook("MacBook", 8, 13, 10, "M1", 10))
    laptops.add_laptop(UltraBook("HP", 8, 13, 10, 1.5, 1))
    laptops.add_laptop(GamingLaptop("Dell", 32, 16.2, 6, "GTX", 4))
    for laptop in laptops.laptops:
        print(laptop)
    print("Our laptops with choosed ram is:\n ")
    laptops1 = laptops.choose_laptop_with_ram(8)
    for laptop in laptops1:
        print(laptop)
    print("Our laptops with screen size more than choosed: \n")
    laptops2 = laptops.find_laptop_with_more_screen_size(15.0)
    for laptop in laptops2:
        print(laptop)
