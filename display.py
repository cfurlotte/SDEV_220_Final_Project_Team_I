import tkinter as tk
from inventory import Inventory
import pickle

class Display(Inventory):
    def __init__(self):
        
        Inventory.__init__(self)
        #global vars go here, there are access to all vars in inventory 
        
    #main code goes here so that I can call it to run when button is pressed.
    def runDisplay(self):
        self.display = tk.Tk()
        #code for inventory starts here
        self.labelInfo = tk.Label(self.display, text = 'All ingredients amounts are in ounces.')
        self.labelInfo.grid(row=0, column=1, columnspan=3)

        '''Dough'''
        self.labelDough = tk.Label(self.display, text = 'Dough Amount: ')
        self.labelDough.grid(row=1, column=1)

        self.displayDough = tk.Label(self.display, text = str(self.inventory['Dough']['current']))
        self.displayDough.grid(row=1, column=2)

        '''Tomato Sauce'''
        self.labelTomatoSauce = tk.Label(self.display, text ='Tomato Sauce Amount')
        self.labelTomatoSauce.grid(row=2, column=1)

        self.displayTomatoSauce = tk.Label(self.display, text = str(self.inventory['TomatoSauce']['current']))
        self.displayTomatoSauce.grid(row=2, column=2)

        '''Cheese'''
        self.labelCheese = tk.Label(self.display, text = 'Cheese Amount: ')
        self.labelCheese.grid(row=3, column=1)

        self.displayCheese = tk.Label(self.display, text = str(self.inventory['Cheese']['current']))
        self.displayCheese.grid(row=3, column=2)

        '''Olive Oil'''
        self.labelOliveOil = tk.Label(self.display, text = 'Olive Oil Amount: ')
        self.labelOliveOil.grid(row=4, column=1)

        self.displayOliveOil = tk.Label(self.display, text = str(self.inventory['OliveOil']['current']))
        self.displayOliveOil.grid(row=4, column=2)

        

        #code for inventory ends here
        self.display.mainloop()


