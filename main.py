import tkinter as tk
from gui import GUI
#from inventory import Inventory
from display import Display

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
        


    def calculate(self):
        self.selectedPizzaSize = self.pizzaSizeInfo.get()
        if self.selectedPizzaSize == 'Small':
            self.changeDoughAmount(3)
    def displayDisplay(self):
        self.runDisplay()
    
Main()