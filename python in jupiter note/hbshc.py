# salary = int(input("Enter your salary: "))
# year= int(input("Enter yor working years: "))
# if  year>5:
#     a = salary*(5/100)    
# print(f"your bonus is {a} and net salary is {a+salary}" )    

print("the ticket price is 1000")
age= int((input("Enter your age for discount: ")))
if age>=6 and age<=14:
    print("ticket is free for you")
elif age>=15 and age<=23:
    print(f"the discount for you is {1000*50/100} and net price is {1000-(1000*50/100)}  ")