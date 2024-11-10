class employee:
    company = "Google"

    def showdetails(self):
        print("this is an employee")


class programmer(employee):
    language = "Python"
    company = "youtube"
    def getlanguage(self):
        print(f"the language is {self.language}")
    def showdetails(self):
        print("this is an programer")
e = employee()  
e.showdetails()
p  = programmer()
p.showdetails()
print(p.company)

