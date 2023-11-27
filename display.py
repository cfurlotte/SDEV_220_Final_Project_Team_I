import tkinter as tk
from inventory import Inventory

class Display(Inventory):
    def __init__(self):
        Inventory.__init__(self)
        #global vars go here, there are access to all vars in inventory 
        
    #main code goes here so that I can call it to run when button is pressed.
    def runDisplay(self):
        self.display = tk.Tk()
        #code for inventory starts here


        #code for inventory ends here
        self.display.mainloop()


