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

        self.changeDough = tk.Button(self.display, text = 'Resupply Dough', command = lambda: self.change_inventory(self.inventory, 'Dough', self.inventory['Dough']['max'] - self.inventory['Dough']['current']))
        self.changeDough.grid(row=1, column=3)
        
        '''Tomato Sauce'''
        self.labelTomatoSauce = tk.Label(self.display, text ='Tomato Sauce Amount')
        self.labelTomatoSauce.grid(row=2, column=1)

        self.displayTomatoSauce = tk.Label(self.display, text = str(self.inventory['TomatoSauce']['current']))
        self.displayTomatoSauce.grid(row=2, column=2)


        self.changeTomatoSauce = tk.Button(self.display, text = 'Resupply Tomato Sauce', command = lambda: self.change_inventory(self.inventory, 'TomatoSauce', self.inventory['TomatoSauce']['max'] - self.inventory['TomatoSauce']['current']))
        self.changeTomatoSauce.grid(row=2, column=3)

        '''Cheese'''
        self.labelCheese = tk.Label(self.display, text = 'Cheese Amount: ')
        self.labelCheese.grid(row=3, column=1)

        self.displayCheese = tk.Label(self.display, text = str(self.inventory['Cheese']['current']))
        self.displayCheese.grid(row=3, column=2)

        self.changeCheese = tk.Button(self.display, text = 'Resupply Cheese', command = lambda: self.change_inventory(self.inventory, 'Cheese', self.inventory['Cheese']['max'] - self.inventory['Cheese']['current']))
        self.changeCheese.grid(row=3, column=3)

        '''Olive Oil'''
        self.labelOliveOil = tk.Label(self.display, text = 'Olive Oil Amount: ')
        self.labelOliveOil.grid(row=4, column=1)

        self.displayOliveOil = tk.Label(self.display, text = str(self.inventory['OliveOil']['current']))
        self.displayOliveOil.grid(row=4, column=2)

        self.changeOliveOil = tk.Button(self.display, text = 'Resupply Olive Oil', command = lambda: self.change_inventory(self.inventory, 'OliveOil', self.inventory['OliveOil']['max'] - self.inventory['OliveOil']['current']))
        self.changeOliveOil.grid(row=4, column=3)

        '''Pepperoni'''
        self.labelPepperoni = tk.Label(self.display, text = 'Pepperoni Amount: ')
        self.labelPepperoni.grid(row=5, column=1)

        self.displayPepperoni = tk.Label(self.display, text = str(self.inventory['Pepperoni']['current']))
        self.displayPepperoni.grid(row=5, column=2)

        self.changePepperoni = tk.Button(self.display, text = 'Resupply Pepperoni', command = lambda: self.change_inventory(self.inventory, 'Pepperoni', self.inventory['Pepperoni']['max'] - self.inventory['Pepperoni']['current']))
        self.changePepperoni.grid(row=5, column=3)

        '''Sausage'''
        self.labelSausage = tk.Label(self.display, text = 'Sausage Amount: ')
        self.labelSausage.grid(row=6, column=1)

        self.displaySausage = tk.Label(self.display, text = str(self.inventory['Sausage']['current']))
        self.displaySausage.grid(row=6, column=2)

        self.changeSausage = tk.Button(self.display, text = 'Resupply Sausage', command = lambda: self.change_inventory(self.inventory, 'Sausage', self.inventory['Sausage']['max'] - self.inventory['Sausage']['current']))
        self.changeSausage.grid(row=6, column=3)

        '''Ham'''
        self.labelHam = tk.Label(self.display, text = 'Ham Amount: ')
        self.labelHam.grid(row=7, column=1)

        self.displayHam = tk.Label(self.display, text = str(self.inventory['Ham']['current']))
        self.displayHam.grid(row=7, column=2)

        self.changeHam = tk.Button(self.display, text = 'Resupply Ham', command = lambda: self.change_inventory(self.inventory, 'Ham', self.inventory['Ham']['max'] - self.inventory['Ham']['current']))
        self.changeHam.grid(row=7, column=3)

        '''Mushrooms'''
        self.labelMushrooms = tk.Label(self.display, text = 'Mushrooms Amount: ')
        self.labelMushrooms.grid(row=8, column=1)

        self.displayMushrooms = tk.Label(self.display, text = str(self.inventory['Mushrooms']['current']))
        self.displayMushrooms.grid(row=8, column=2)

        self.changeMushrooms = tk.Button(self.display, text = 'Resupply Mushrooms', command = lambda: self.change_inventory(self.inventory, 'Mushrooms', self.inventory['Mushrooms']['max'] - self.inventory['Mushrooms']['current']))
        self.changeMushrooms.grid(row=8, column=3)

        '''Onions'''
        self.labelOnions = tk.Label(self.display, text = 'Onions Amount: ')
        self.labelOnions.grid(row=9, column=1)

        self.displayOnions = tk.Label(self.display, text = str(self.inventory['Onions']['current']))
        self.displayOnions.grid(row=9, column=2)

        self.changeOnions = tk.Button(self.display, text = 'Resupply Onions', command = lambda: self.change_inventory(self.inventory, 'Onions', self.inventory['Onions']['max'] - self.inventory['Onions']['current']))
        self.changeOnions.grid(row=9, column=3)

        '''Peppers'''
        self.labelPeppers = tk.Label(self.display, text = 'Peppers Amount: ')
        self.labelPeppers.grid(row=10, column=1)

        self.displayPeppers = tk.Label(self.display, text = str(self.inventory['Peppers']['current']))
        self.displayPeppers.grid(row=10, column=2)

        self.changePeppers = tk.Button(self.display, text = 'Resupply Peppers', command = lambda: self.change_inventory(self.inventory, 'Peppers', self.inventory['Peppers']['max'] - self.inventory['Peppers']['current']))
        self.changePeppers.grid(row=10, column=3)

        self.refreshWindow = tk.Button(self.display, text = 'Refresh Inventory', command=self.resetWindow)
        self.refreshWindow.grid(row=11, column=2)

        #code for inventory ends here
        self.display.mainloop()

    def resetWindow(self):
        self.display.destroy()
        self.runDisplay()


