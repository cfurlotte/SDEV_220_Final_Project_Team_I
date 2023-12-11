import pickle

class Ingredient:
    def __init__(self, name, current, max):
        # Initialize an Ingredient object with a name, current quantity, and maximum quantity
        self.name = name
        self.current = current
        self.max = max

    def change(self, amount):
        # Change the current quantity of the ingredient by the specified amount
        self.current == amount

    def reset(self):
        # Reset the current quantity of the ingredient to its maximum quantity
        self.current = self.max

class Inventory:
    def __init__(self, ingredients):
        # Initialize an Inventory object with a list of ingredients
        self.ingredients = ingredients

    def save(self):
        # Save the ingredients list to a file named 'inventory.pkl' using pickle
        with open('inventory.pkl', 'wb') as f:
            pickle.dump(self.ingredients, f)

    def load(self):
        try:
            # Load the ingredients list from the file 'inventory.pkl' using pickle
            with open('inventory.pkl', 'rb') as f:
                self.ingredients = pickle.load(f)
        except FileNotFoundError:
            # If the file is not found, set the ingredients list to an empty list
            self.ingredients = []

if __name__ == "__main__":
    # Create a list of Ingredient objects
    ingredients = [
        Ingredient('Dough', 25, 500),
        Ingredient('TomatoSauce', 25, 300),
        Ingredient('Cheese', 25, 300),
        Ingredient('OliveOil', 25, 100),
        Ingredient('Pepperoni', 25, 100),
        Ingredient('Sausage', 25, 100),
        Ingredient('Ham', 25, 100),
        Ingredient('Mushrooms', 25, 75),
        Ingredient('Onions', 25, 75),
        Ingredient('Peppers', 25, 75),
    ]
    # Create an Inventory object with the list of ingredients
    inventory = Inventory(ingredients)
    # Save the inventory to a file
    inventory.save()
