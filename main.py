

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
        
        #two temp buttons to take and show where the code for them goes, can be a function in GUI that is just called here instead.
        self.submitButton = tk.Button(self.window, text = 'Order', command = lambda: self.calculate()).pack()
        self.displayButton = tk.Button(self.window, text = 'Inventory', command = lambda: self.displayDisplay()).pack()

        #code goes above this line
        self.runGUI()
        

    #is called when user hits the order button
    def calculate(self):
        #gets the info of different selections
        self.selectedPizzaSize = self.pizzaSizeInfo.get()
        #calculates the amount of dough that the pizza order will use and removes it from inventory
        if self.selectedPizzaSize == 'Small':
            self.change_inventory(self.inventory, 'Dough', -3)
        self.save_inventory(self.inventory)
    def displayDisplay(self):
        self.runDisplay()
    
Main()