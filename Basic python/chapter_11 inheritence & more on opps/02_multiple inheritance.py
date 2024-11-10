class employee:
    company = "visa"
    ecode =120


class freelancher:
    company  ="fiver"
    level = 0

    def upgradelevel(self):
        self.level = self.level + 1

class programmer(employee, freelancher): # yaha par employee pahle  likha aur freelancher bad me likha isliye company visa print hui hai
    name = "Rohit"

p = programmer() 
p.upgradelevel()  
print(p.level)   
print(p.company)  