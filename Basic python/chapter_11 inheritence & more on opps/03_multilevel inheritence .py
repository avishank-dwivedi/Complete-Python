class person :
    country ="India"

    def takebreth(self):
        print("I am brething....")

class employee(person):
    company = "honda"        

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def takebreth(self):
        print("I am an Employee so I am luckyly breathing..")  

class programmer(employee):
    company = "fiver"
    def getsalary(self):
        print(f"No salary to programmer")
    def takebreth(self):
        print("I am a programmer so I am breathing + + +..")      

p = person()
p.takebreth()
#print(p.company) # throws an error
e = employee()
e.takebreth()
print(e.company)
pr = programmer()
pr.takebreth()
print(pr.company)
print(pr.country)




