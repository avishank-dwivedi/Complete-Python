import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType= "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"train is {self.train}")

ganeshApplication = RailwayForm()    
ganeshApplication.name="Ganesh"   
ganeshApplication.train="Vande Bharat "  
ganeshApplication.printData() 
