# Import a few useful containers from the typing module
from typing import Dict, Union, Optional

class Computer:

    # What attributes will it need?
 #processor_type, hard_drive_capacity, memory, operating_system, year_made, price
    

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, name, processor_type, hard_drive_capacity, memory, operating_system, year_made, 
    price):
        self.name = name
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # Refurbish
    def refurbish(self, new_os: Optional[str] = None):
        
            if self.year_made < 2000:
                self.price = 0 # too old to sell, donation only
            elif self.year_made < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
            elif self.year_made < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.price = 1000 # recent stuff

            if new_os is not None:
                self.operating_system = new_os # update details after installing new OS
    #update_price
    #print_computer_details
    #update_os
    
    # update price
    def update_price(self, new_price: int):
       self.price = new_price

    def check_price(self):
        print(self.price)

    def print_computer_details(self):
        print("Computer name:", self.name),
        print("Hard Drive Capacity:", self.hard_drive_capacity),
        print("Processor type:", self.processor_type),
        print("Memory:", self.memory),
        print("Operating System:", self.processor_type),
        print("Year Made:", self.year_made),
        print("Price:", self.price)

    # What methods will you need?


my_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 0)

egg_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2020, 2900)


egg_computer.print_computer_details()










