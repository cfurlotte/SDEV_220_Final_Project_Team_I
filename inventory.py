class Inventory:
    def __init__(self):
        #Charles code to show way program works
        #max amount of a product
        self.maxDough = 500 #oz
        #current amount, should be stored in a file, or create a file if file does not exist
        self.currentDough = self.maxDough

        
    #example layout of a function I can call to change amount of something.
    def changeDoughAmount(self, amountToChange):
        self.currentDough -= amountToChange
        print(self.currentDough)