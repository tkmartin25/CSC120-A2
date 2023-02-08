# Import a few useful containers from the typing module
from typing import Dict, Union, Optional

from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory : Dict = {}
    itemID: int = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    
    def __init__(self, inventory, name : str, location: Optional[str] = None):
        self.inventory = inventory
        self.name = name
        self.location = None
        # location is optional
        if location is not None:
            self.location = location
   
    # buy computer and assign item ID to computer
    def buy(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        print(self.itemID, computer, "was bought for the price of", computer.price, "dollars.")

    # sell computer
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # printing inventory and computer details
    def print_inventory(self):
    # If the inventory is not empty
        if len(self.inventory) >= 1:
        # For each item
            for item_id in self.inventory:
            # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
                computer = self.inventory[item_id]
                computer.print_computer_details()
        else:
            print("No inventory to display.")
    
    # update price according to computer condition and update OS
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
            
            # update O.S. -- optional
            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    # check price of computer using item id
    def check_price(self, item_id):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            print("The price is", computer.price, "dollars.")
        else:
            print("Item", item_id, "not found. Cannot check price.")

    # update price of computer using item id and new price as arguments
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            computer.price = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
    # print shop details (location and name of shop)
    def print_shop_details(self):
        if self.location is not None:
            print("This shop is called", self.name + ",", "which is located in", self.location + ".")
            print(self.name, "currently has", len(self.inventory), "computer(s).")
        else:
            print("This shop is called", self.name + ".")
    
    


# What methods will you need?
    # buy computer, sell computer, print inventory, refurbish computer, update price, check price
# Testing Code

# Create Resale shop
Lucretia_shop = ResaleShop({}, "Lucretia's Shop", "Bass Hall, Smith College")

# buy computers
Lucretia_shop.buy(ally_computer)

Lucretia_shop.buy(egg_computer)

# refurbish computer

Lucretia_shop.refurbish(2)

# check price computer and update it
Lucretia_shop.check_price(2)

Lucretia_shop.update_price(2, 800)

Lucretia_shop.check_price(2)

# print shop details
Lucretia_shop.print_shop_details()

# sell computer
Lucretia_shop.sell(2)

# print inventory
Lucretia_shop.print_inventory()
