#1--------> write a program to print multiplication table of a given number using for loop
'''num = int(input("Enter the number: "))
for i in range(1,11):
    # print(str(num) + "X" + str(i) + "=" + str(i*num))
      print(f"{num}X{i}={num*i}")'''
#2----->attempt problem using while loop 
'''num = int(input("Enter the number: "))
i = 1
print("The multiplication Table of :", num)
while i <= 10:
    num = num*1
    print(num, 'X', i ,'=', num*i)
    i+=1'''
#3---->write a program to greet all the person names starts in a list l1 and which starts with S l1=["Harry", "sohan", "sapna", "Rahul"]
'''l1= ["Harry", "Sohan", "Sapna", "Rahul"] 

for name in l1:
    if name.startswith("S"):
        print("Hello "+ name)'''

#04---->write a  program to find that a give number is prime or not
'''num = int(input("Enter your number: "))
prime = True

for i in range (2, num ):
    if(num%i==0):
        prime= False
        break
if prime:    
        print("This number is prime.")
else:
     print("this number is not  Prime") '''

#05---->Write  a program to find the sum of first n natural number using for loop
'''num = int(input("Please enter  your end number: "))
sum = 0
for value in range(1, num+1):
    sum=sum+value

print(sum)'''
#06------>Write  a program to find the sum of first n natural number using while loop
'''num = int(input("Enter your number: "))
if num<0:
    print("Enter a positive number")
else:
    sum = 0
    while(num>0):
        sum+=num
        num-=1
print("The sum is", sum)'''
#07------->Write a program to find the factorial of a given number using for loop
'''num = int(input("Enter the number: ")) 
factorial =  1           
for i in range(1, num+1):  #ek is lekar given no. tak jay
    factorial = factorial*i
      
print(f"The factorial of {num} number is {factorial}")'''
#08 write a program to print this pattern
# *
# **
# *** for n = 3
'''n = 4 

for i in range (4):
    print("*" * (i+1))'''

#09 write a program to print this pattern
#   *
#  ***
# ***** for n = 3
'''n = 3
for i  in range(3):
    print(" " * (n-i-1), end="" )
    print("*" * (2*i+1), end= "")
    print(" " * (n-i-1))'''
#10write a program to print this pattern/////ask some one 
# * * *
# *   *
# * * *   for n = 3
'''n= 3
for i in range(3):
    print("*")'''
#11 write  a program to print multiplication table of n using for loop in reverse order

table  = int(input("Enter the table: "))
limit = (int(input("Enter the ending : ")))
for i in range( limit,0,-1):
    # print(str(num) + "X" + str(i) + "=" + str(i*num))
      print(f"{table}X{i}={table*i}")
                   


  
    

    
      
        

     


        

            


       




        


