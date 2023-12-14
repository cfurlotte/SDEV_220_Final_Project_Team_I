''''''
import tkinter as tk
from gui import GUI
#from inventory import Inventory
from display import Display
import pickle


class Main(GUI, Display):
    def __init__(self):
        GUI.__init__(self)
        #Inventory.__init__(self)
        Display.__init__(self)
        
        #two temp buttons to take and show where the code for them goes, can be a function in GUI that is just called here instead.d
        self.submitButton = tk.Button(self.window, text = 'Order', command = lambda: self.calculate(), width=11, height=1)
        self.submitButton.grid(row=15, column=2, ipadx=40, ipady=10, pady=10, padx=85)
        self.displayButton = tk.Button(self.window, text = 'Inventory', command = lambda: self.displayDisplay(), width=11, height=1)
        self.displayButton.grid(row=16, column=2, ipadx=40, ipady=1, pady=1, padx=85)

        #code goes above this line
        self.runGUI()
        
    '''runs when the order button is pressed'''
    #is called when user hits the order button
    def calculate(self):
        #gets the info of different selections
        self.selectedPizzaSize = self.pizzaSizeInfo.get()
        #calculates the amount of dough, TomatoSauce, cheese, and oliveOil that the pizza order will use and removes it from inventory
        if self.selectedPizzaSize == 'Small':
            self.change_inventory(self.inventory, 'Dough', -3)
            self.change_inventory(self.inventory, 'TomatoSauce', -1)
            self.change_inventory(self.inventory, 'Cheese', -2)
            self.change_inventory(self.inventory, 'OliveOil', -1)
            if self.pizzaPepperoniInfo == True:
                self.change_inventory(self.inventory, 'Pepperoni', -1)
            if self.pizzaSausageInfo == True:
                self.change_inventory(self.inventory, 'Sausage', -1)
            if self.pizzaHamInfo == True:
                self.change_inventory(self.inventory, 'Ham', -1)
            if self.pizzaMushroomInfo == True:
                self.change_inventory(self.inventory, 'Mushroom', -1)
            if self.pizzaOnionsInfo == True:
                self.change_inventory(self.inventory, 'Onions', -1)
            if self.pizzaPepperInfo == True:
                self.change_inventory(self.inventory, 'Pepper', -1)
        elif self.selectedPizzaSize == 'Medium':
            self.change_inventory(self.inventory, 'Dough', -6)
            self.change_inventory(self.inventory, 'TomatoSauce', -2)
            self.change_inventory(self.inventory, 'Cheese', -4)
            self.change_inventory(self.inventory, 'OliveOil', -2)
            if self.pizzaPepperoniInfo == True:
                self.change_inventory(self.inventory, 'Pepperoni', -2)
            if self.pizzaSausageInfo == True:
                self.change_inventory(self.inventory, 'Sausage', -2)
            if self.pizzaHamInfo == True:
                self.change_inventory(self.inventory, 'Ham', -2)
            if self.pizzaMushroomInfo == True:
                self.change_inventory(self.inventory, 'Mushroom', -2)
            if self.pizzaOnionsInfo == True:
                self.change_inventory(self.inventory, 'Onions', -2)
            if self.pizzaPepperInfo == True:
                self.change_inventory(self.inventory, 'Pepper', -2)
        elif self.selectedPizzaSize == 'Large':
            self.change_inventory(self.inventory, 'Dough', -12)
            self.change_inventory(self.inventory, 'TomatoSauce', -4)
            self.change_inventory(self.inventory, 'Cheese', -8)
            self.change_inventory(self.inventory, 'OliveOil', -4)
            if self.pizzaPepperoniInfo == True:
                self.change_inventory(self.inventory, 'Pepperoni', -4)
            if self.pizzaSausageInfo == True:
                self.change_inventory(self.inventory, 'Sausage', -4)
            if self.pizzaHamInfo == True:
                self.change_inventory(self.inventory, 'Ham', -4)
            if self.pizzaMushroomInfo == True:
                self.change_inventory(self.inventory, 'Mushroom', -4)
            if self.pizzaOnionsInfo == True:
                self.change_inventory(self.inventory, 'Onions', -4)
            if self.pizzaPepperInfo == True:
                self.change_inventory(self.inventory, 'Pepper', -4)

        self.save_inventory(self.inventory)
    def displayDisplay(self):
        self.runDisplay()
    
Main()