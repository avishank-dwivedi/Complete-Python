#1--->write a program using function to find greatest of three numbers
'''def maximum(num1,num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else: return num3
    else:  
        if(num2>num3):
            return num2
        else: return num3 


m = maximum(3, 5, 142)
print(m)'''

#2----> write a program to celcius to fahrenheit
'''def farh(cel):
    return (cel *(9/5)) + 32

c = 0
f = farh(c)
print("Fahrenheit Temerature is " + str(f))'''
#3 -----> write a program to prevent a python print ()function to print a new line at the end
'''print("helllo", end=" ")
print("how", end=" ")
print("are", end=" ")
print("you?", end=" ")'''

#4 write a recursive function to calculate the sum of first n natural number
''''def SumofN(k):
    s= 0
    for i in range(1,k+1):
        s +=i
    return s    
print("Enter the value of n: ", end ="")
try:
    n = int(input())
    if n<0:
        print("\n Invalid Input!")
    else:
        sum = SumofN(n)
        print("\nSum = ", sum)
except ValueError:
    print("\nInvalid Input!")  '''
#5 write a program to find sum of n natural number using recursive function....
'''def sum_number(n):
    result = 0
    if n ==1:
        result=1
    else:
        result = n+sum_number(n-1) #this means n + sum of n-1 = sum of n 
    return result          
    
n = int(input("Enter yorn n: "))
Sum = sum_number(n)   
print(f"Sum of first (n) numbers : {Sum}")'''

#6 write a program to print following pattern...
# ***
# **
# *      for n =3 
'''n = 3
for i in range(n):
    print("*" * (n-i))'''
#7 write a python function which converts inches to cms 
'''def cms(inch):
    return (inch*2.54)

I= int(input("Enter your inch lenth: "))
C = cms(I)
print(f"cms lenth is "+ str(C))'''
#8 write a python program to remove a give word from a string and strip it at the same time...
'''def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "      Ganesh is a good boy      "
n = remove_and_strip(this, "Ganesh")
print(n)'''
#9---->write a program to print the mutiplication table of a given number
def mul_table(N, i):
    if(i>10):
        return
    print(N,"*",i,"=", N *i)
    return mul_table(N,i+1)
N=8
mul_table(N,1)
    
    



    
    