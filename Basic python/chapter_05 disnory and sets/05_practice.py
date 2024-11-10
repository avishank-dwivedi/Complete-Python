#1-------->write a program to create a dictionary of Hindi words with values as their english tranlation provide user with an option to look it up...
'''mydict= {
    "pankha": "fan",
    "dabba":"box",
    "rui":"cotton"

}
print("Options are ", mydict.keys())
a = input("enter the hindi word\n")
print("The meaning of your word is :", mydict.get(a))'''
#2----->write a program to input eight number from the user and display all the unique numbers (once)....
'''num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
num4 = int(input("Enter num4:"))
num5 = int(input("Enter num5:"))
num6 = int(input("Enter num6:"))
num7 = int(input("Enter num7:"))
num8 = int(input("Enter num8:"))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)'''
#3-------> can we have a set with 18(int) and 18(str) as a value in it 
'''s = {18, "18"}
print(s)'''
#4---> what will the lenth of following this set.....
'''s = set()
s.add(20)
s.add(20.0)#this is same as 20
s.add("20")
print(len(s))'''
#5----->type of s = {}
'''s ={}
print(type(s))'''# empty set = () and empty dictionary is s ={}...
#6-----> create a empty dictionary and allow 4 friend to enter their favourite language assume they are unique........
'''favlang = {}
a = input("enter your favourite language Aman: ")
b = input("enter your favourite language Dhanraj: ")
c  = input("enter your favourite language Devansh: ")
d  = input("enter your favourite language Avishank: ")
favlang["Aman"] =a
favlang["Dhanraj"]= b
favlang["Devansh"]= c
favlang["Avishank"]= d

print(favlang)'''
#7----->if the two names are common in the friend list

'''favlang = {}
a = input("enter your favourite language Aman: ")
b = input("enter your favourite language Dhanraj: ")
c  = input("enter your favourite language Devansh: ")
d  = input("enter your favourite language Avishank: ")
favlang["Aman"] =a
favlang["Aman"]= b
favlang["Devansh"]= c
favlang["Avishank"]= d

print(favlang)'''
#8---->if two languages are same
'''favlang = {}
a = input("enter your favourite language Aman: ")
b = input("enter your favourite language Dhanraj: ")
c  = input("enter your favourite language Devansh: ")
d  = input("enter your favourite language Avishank: ")
favlang["Aman"] =a
favlang["Dhanraj"]= b
favlang["Devansh"]= c
favlang["Avishank"]= d

print(favlang)'''
#9----->can we change the value inside a list which is in set 
'''s= {8, 7, 12, "Ganesh", [1,2]}# it will throws an error
print(s)'''# it cannot be changed because it has tupple inside .... 