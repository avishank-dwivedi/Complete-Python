class employee:
    company="Bharat gas"
    salary = 4500
    salarybonus=600
    # totalsalary= 5000
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val -self.salary
    

e = employee()
print(e.totalsalary)
e.totalsalary = 5600
print(e.totalsalary)
print(e.salarybonus)

