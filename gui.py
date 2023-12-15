'''Code to create the order form of the Application, written by Charles'''
import tkinter as tk
class GUI:
    def __init__(self):
        #Charles code to show how program works

        '''Code to create the window'''
        #create main window
        self.window = tk.Tk()
        #change size of the main window
        self.window.geometry('346x420')
        #title for the window
        self.window.title('Order Form')
        #changes the background color of {self.window}
        self.window.config(bg='#999')
        
        '''Code to create a gap at the top of {self.window}'''
        #create a label to center the other elements
        #self.label = tk.Label(self.window, text = " ", bg='#999')
        #self.label.grid(row=1, column=1, ipadx=40)
        #label to take and create a margin at the top of the screen
        self.labelTop = tk.Label(self.window, text = " ", bg='#999')
        self.labelTop.grid(row=0, column=2, ipady=1)
        
        '''Code for getting the order and displaying the order options'''
        #stores pizza size
        self.pizzaSizeInfo = tk.StringVar()
        #set default pizza size
        self.pizzaSizeInfo.set('Medium')
        #list of pizza options
        self.pizzaSizeOptions = ['Small', 'Medium', 'Large']
        #show pizza options
        self.pizzaSize = tk.OptionMenu(self.window, self.pizzaSizeInfo, *self.pizzaSizeOptions)
        self.pizzaSize.grid(row=1, column=2, ipadx=40, ipady=10, pady=10, padx=85)

        #displays some instructions
        self.pizzaInstructions = tk.LabelFrame(self.window, text="Toppings.")
        self.pizzaInstructions.grid(row=2, column=2, ipadx=39, ipady=1, pady=10, padx=85)

        #stores if the person ordering wants Pepperoni
        self.pizzaPepperoniInfo = False
        #temp var so that checkbutton does not get linked
        self.temp1 = tk.BooleanVar
        #displays a checkbox for weather they want peperoni or not
        self.pizzaPepperoniOption =  tk.Checkbutton(self.pizzaInstructions, text = "Pepperoni", variable=self.temp1, command=lambda: self.PeperoniBoolean())
        self.pizzaPepperoniOption.grid(row=3, column=2, sticky='w')

        #stores if the person ordering wants Sausage
        self.pizzaSausageInfo = False
        #temp var so that checkbutton does not get linked.
        self.temp2 = tk.BooleanVar
        #displays a checkbox for weather they want Sausage or not
        self.pizzaSausageOption = tk.Checkbutton(self.pizzaInstructions, text = "Sausage", variable=self.temp2, command=lambda: self.SausageBoolean())
        self.pizzaSausageOption.grid(row=4, column=2, sticky='w')

        #stores if the person ordering wants Ham
        self.pizzaHamInfo = False
        #temp var so that checkbutton does not get linked.
        self.temp3 = tk.BooleanVar
        #displays a checkbox for weather they want Ham or not
        self.pizzaHamOption = tk.Checkbutton(self.pizzaInstructions, text = "Ham", variable=self.temp3, command=lambda: self.HamBoolean())
        self.pizzaHamOption.grid(row=5, column=2, sticky='w')

        #stores if the person ordering wants Mushroom
        self.pizzaMushroomInfo = False
        #temp var so that checkbutton does not get linked.
        self.temp4 = tk.BooleanVar
        #displays a checkbox for weather they want Mushroom or not
        self.pizzaMushroomOption = tk.Checkbutton(self.pizzaInstructions, text = "Mushroom", variable=self.temp4, command=lambda: self.MushroomBoolean())
        self.pizzaMushroomOption.grid(row=6, column=2, sticky='w')

        #stores if the person ordering wants Onions
        self.pizzaOnionsInfo = False
        #temp var so that checkbutton does not get linked.
        self.temp4 = tk.BooleanVar
        #displays a checkbox for weather they want Onions or not
        self.pizzaOnionsOption = tk.Checkbutton(self.pizzaInstructions, text = "Onions", variable=self.temp4, command=lambda: self.OnionsBoolean())
        self.pizzaOnionsOption.grid(row=7, column=2, sticky='w')

        #stores if the person ordering wants Peppers
        self.pizzaPeppersInfo = False
        #temp var so that checkbutton does not get linked.
        self.temp6 = tk.BooleanVar
        #displays a checkbox for weather they want Peppers or not
        self.pizzaPeppersOption = tk.Checkbutton(self.pizzaInstructions, text = "Peppers", variable=self.temp6, command=lambda: self.PeppersBoolean())
        self.pizzaPeppersOption.grid(row=8, column=2, sticky='w')

        
    '''code for booleans for the check boxes for options on the pizza'''
    def PeperoniBoolean(self):
        if self.pizzaPepperoniInfo == False:
            self.pizzaPepperoniInfo = True
        else:
            self.pizzaPepperoniInfo = False
    def SausageBoolean(self):
        if self.pizzaSausageInfo == False:
            self.pizzaSausageInfo = True
        else:
            self.pizzaSausageInfo = False
    def HamBoolean(self):
        if self.pizzaHamInfo == False:
            self.pizzaHamInfo = True
        else:
            self.pizzaHamInfo = False
    def MushroomBoolean(self):
        if self.pizzaMushroomInfo == False:
            self.pizzaMushroomInfo = True
        else:
            self.pizzaMushroomInfo = False
    def OnionsBoolean(self):
        if self.pizzaOnionsInfo == False:
            self.pizzaOnionsInfo = True
        else:
            self.pizzaOnionsInfo = False
    def PeppersBoolean(self):
        if self.pizzaPeppersInfo == False:
            self.pizzaPeppersInfo = True
        else:
            self.pizzaPeppersInfo = False
        
        
    #run mainloop() is called at the and of Main __init__(self)
    def runGUI(self):
        self.window.mainloop()
