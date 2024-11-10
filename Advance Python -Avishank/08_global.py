a =54 # Global variable
def func1():
    global a # this forces to use global variable 'a'.
    print(f"print statement 1:{a} ")
    a=7# Local Variable
    print(f"print statement 2:{a} ")
func1() 
print(f"print statement 3:{a} ")  