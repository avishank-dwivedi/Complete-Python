class person :
    country ="India"
    def __init__(self):
        print("Initializing Person....\n")

    def takebreth(self):
        print("I am brething....")

class employee(person):
    company = "honda" 
    def __init__(self):
        super().__init__()
        print("Initializing employee....\n")       

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takebreth(self):
        super().takebreth()
        print("I am an Employee so I am luckyly breathing..")  

class programmer(employee):
    company = "fiver"
    def __init__(self):
        super().__init__()
        print("Initializing Programmer....\n")
    def getsalary(self):
        print(f"No salary to programmer")
    def takebreth(self):
        super().takebreth()
        print("I am a programmer so I am breathing + + +..")      

# p = person()
# p.takebreth()

# e = employee()
# e.takebreth()


pr = programmer()
# pr.takebreth()





