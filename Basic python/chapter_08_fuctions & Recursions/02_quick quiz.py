def greet(name):
    print("Good Day, " + name)# this is function definition
        
greet("Ganesh")# this is function calling

def mysum(num1, num2):
    return num1 + num2

s =mysum(6, 35)
print(s)
def greet(name = "stranger"): # this is default parameter value
    print("Good Day, " + name)
        
greet()