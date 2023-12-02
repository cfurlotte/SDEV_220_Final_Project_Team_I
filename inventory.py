import pickle

def load_inventory():
    try:
        with open('inventory.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}

def save_inventory(inventory):
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(inventory, f)

def change_inventory(inventory, item, amount):
    if item in inventory:
        inventory[item]['current'] += amount
    else:
        print(f"Item {item} not found in inventory.")
    save_inventory(inventory)

def reset_inventory(inventory, item):
    if item in inventory:
        inventory[item]['current'] = inventory[item]['max']
    else:
        print(f"Item {item} not found in inventory.")
    save_inventory(inventory)

if __name__ == "__main__":
    inventory = {
        'Dough': {'current': 25, 'max': 500},
        'TomatoSauce': {'current': 25, 'max': 300},
        'Cheese': {'current': 25, 'max': 300},
        'OliveOil': {'current': 25, 'max': 100},
        'Pepperoni': {'current': 25, 'max': 100},
        'Sausage': {'current': 25, 'max': 100},
        'Ham': {'current': 25, 'max': 100},
        'Mushrooms': {'current': 25, 'max': 75},
        'Onions': {'current': 25, 'max': 75},
        'Peppers': {'current': 25, 'max': 75},
    }
    save_inventory(inventory)
