from gui import GUI
from inventory import Inventory

class Main(GUI, Inventory):
    def __init__(self):
        GUI.__init__(self)
        Inventory.__init__(self)
    
Main()