'''Code to manage Inventory, written by David'''
import pickle

class Inventory:
    def __init__(self):
        self.inventory = self.load_inventory()
        
    #opens the inventory.pkl file and loads the inventory from it.
    def load_inventory(self):
        try:
            with open('inventory.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    #takes the inventory dictionary as an argument and writes the inventory to the inventory.pkl file.
    def save_inventory(self, inventory):
        with open('inventory.pkl', 'wb') as f:
            pickle.dump(inventory, f)

    #Takes the inventory dictionary, item name, and an amount as an argument, it checks if the item is in the inventory, and if it is then it adds the amount to the current amount of the item
    def change_inventory(self, inventory, item, amount):
        if item in inventory:
            inventory[item]['current'] += amount
        else:
            print(f"Item {item} not found in inventory.")
        self.save_inventory(inventory)

    #takes the inventory dictionary as an argument and it checks if the item is in the inventory, and if it is then it sets the amount to the max amount.
    def reset_inventory(self, inventory, item):
        if item in inventory:
            inventory[item]['current'] = inventory[item]['max']
        else:
            print(f"Item {item} not found in inventory.")
        self.save_inventory(inventory)

