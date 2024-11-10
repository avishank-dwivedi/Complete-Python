class Employee:
    company ="Google"
    salary =100
harry = Employee()    
rajni = Employee()
print(harry.company)
print(rajni.company)
harry.salary = 300
rajni.salary = 400
Employee.company="Youtube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)
print(rajni.address)
