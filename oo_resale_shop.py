# Import a few useful containers from the typing module
from typing import Dict, Union, Optional

from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory : Dict = {}
    itemID = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory, name : str):
        self.inventory = inventory
        self.name = name

    def buy(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
        if len(self.inventory) >= 1:
        # For each item
            for item_id in self.inventory:
            # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
    
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discount`ed price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            computer.price = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")


Teddys_shop = ResaleShop({}, "Teddy's Shop")


Teddys_shop.buy(egg_computer)


Teddys_shop.refurbish(1)

Teddys_shop.update_price(2, 200)
egg_computer.print_computer_details()



    

    # What methods will you need?
    # buy computer, sell computer, print inventory, refurbish check
