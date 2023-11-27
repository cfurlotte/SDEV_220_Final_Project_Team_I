import tkinter as tk
class GUI:
    def __init__(self):
        #Charles code to show how program works
        #create main window
        self.window = tk.Tk()
        #stores pizza size
        self.pizzaSizeInfo = tk.StringVar()
        #set default pizza size
        self.pizzaSizeInfo.set('Medium')
        #list of pizza options
        self.pizzaSizeOptions = ['Small', 'Medium', 'Large']
        #show pizza options
        self.pizzaSize = tk.OptionMenu(self.window, self.pizzaSizeInfo, *self.pizzaSizeOptions).pack()
        
        
        
    #run mainloop() is called at the and of Main __init__(self)
    def runGUI(self):
        self.window.mainloop()
