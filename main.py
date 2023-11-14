from gui import GUI
from inventory import Inventory
from display import Display

class Main(GUI, Inventory):
    def __init__(self):
        GUI.__init__(self)
        Inventory.__init__(self)
        Display.__init__(self)
    
Main()