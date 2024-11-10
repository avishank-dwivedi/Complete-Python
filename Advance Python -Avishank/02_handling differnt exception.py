try:
    a = int (input("Enter your name: "))
    c=1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value!")    
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero!")    
    print(e)
print("Thanks for using this this code!")   

#SYNTAX:--->
'''
try:
    #code
except ZerdivisionError:
    #code 
except TypeError:
    #code    -> fill other exception like this

    
    
        
'''