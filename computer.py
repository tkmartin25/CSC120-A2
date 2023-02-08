# Import a few useful containers from the typing module
from typing import Optional

class Computer:

    # What attributes will it need?
    #processor_type, hard_drive_capacity, memory, operating_system, year_made, price

    # How will you set up your constructor?

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description : str, processor_type : str, hard_drive_capacity : int, memory : int, operating_system : str, year_made : int, 
    price : int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # print computer details
    def print_computer_details(self):
        print("Computer Details")
        print("Computer description:", self.description),
        print("Hard Drive Capacity:", self.hard_drive_capacity),
        print("Processor type:", self.processor_type),
        print("Memory:", self.memory),
        print("Operating System:", self.operating_system),
        print("Year Made:", self.year_made),
        print("Price:", self.price)

    # What methods will you need?
    # check computer details

# Testing Code by creating computers
my_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 0)

egg_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2020, 2900)

ally_computer = Computer("Mac Pro 2020", 
        "2 GHz Quad-Core Intel Core i5", 
        2048, 16, "macOS Monterey", 2020, 2000)

# check print_computer_details works

ally_computer.print_computer_details()

