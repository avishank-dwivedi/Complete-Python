#1---->write a program to find greast of four number enterd by user
'''num1  = int(input("enter your num1 :"))
num2  = int(input("enter your num2 :"))
num3  = int(input("enter your num3 :"))
num4  = int(input("enter your num4 :"))

if(num1>num4):
    f1= num1
else:
    f1= num4


if(num2>num3):
    f2= num2
else:
    f2 = num3   


if(f1>f2):
    print(str(f1) + " is greatest") 
else:     
     print(str(f2) + " is greatest") '''

 #2----->write a program to find out wheather a student is pass or fail, if it require total  40% and at least 33% in each subject to pass assume 3 subjects and take marks as an input from the user.
'''sub1 = int(input("Enter your marks of sub1: "))          
sub2 = int(input("Enter your marks of sub2: "))          
sub3 = int(input("Enter your marks of sub3: "))   

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif((sub1+sub2+sub3)/3<40):
    print("You are fail due to total percentage is less  than 40%") 
else:
    print("Congratulation! tou passed the exam.")'''
#3---->A spam comment is definded as a text containing following keywords: "make a lot of money", "nuy now", "subscribe this", "click this", write a program to detect these spams.
'''text  = input("Enter the text ")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam =False

if(spam):
    print("this text is spam!!!")
else:
    print("this text is not spam")'''
#4----> write a program to find that given user name contains less than 10 charactor or  not..
'''name  = input("Enter your name: ")  
print(len(name))


if(len(name)<10):
    print("the chacrector contains less than 10 letter.")
else:
    print("your charector contains 10 or more than 10 letters")''' 
#5----> write a program to find out that the given name is present in alist or not
'''list = ["Ganesh", "Aman", "Dhanraj", "Devansh", "Manas", "Sakshi"] 
name = input("Enter your name.")  

if(name in list):
    print("yes")
else:
    print("no!")'''
#6------> write a program to calculate the grade of a student from his marks from the following scheme: 90-100--ex, 80 - 90 --A, 70-80--B, 60-70--C, 50-60--D,<50--F
'''marks = int(input("Enter your Marks\n"))

if(marks>90):
    grade = "Ex"
elif(marks>=80):
    grade = "A"    
elif(marks>=70):
    grade = "B"    
elif(marks>=60):
    grade = "C"    
elif(marks>=50):
    grade = "D"
else:
    grade = "F"        
print ("Your grade is " + grade ) '''
#7--->write a  program to find out that post is talking about "Ganesh" or not
post = input("Enter your post here!\n")   
if ("GANESH" in post):
    print("You are mentioned.")
elif ("ganesh" in post):
    print("You are mentioned.")
elif ("Ganesh" in post):
    print("You are mentioned.")
else:
    print("You are not mentioned!")    

