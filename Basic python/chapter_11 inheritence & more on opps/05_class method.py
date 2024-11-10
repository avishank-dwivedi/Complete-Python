# class employee:
#     company = "Camel"
#     salary = 100
#     location = "Delhi"

#     # def changesalary(self,sal):
#     #     self.salary=sal
#     #     self.__class__.salary = sal # for changing class attribute
        
#     @classmethod
#     def changesalary(cls, sal):
#         cls.salary = sal

# e = employee()  
# print(e.salary)  
# e.changesalary(455)
# print(e.salary)
# print(employee.salary)# class attribute nhi change hua keval instant attribute  hi change hua hai

p = int(input(" enter p:"))
r = int(input(" enter r:"))
t= int(input(" enter t:"))
i =(p*r*t)/100
print(i)
