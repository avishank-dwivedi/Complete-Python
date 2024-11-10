#1--->write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'
'''f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present.")
else:
    print("twinkle is not present.") 

f.close() '''

#2---->the game() function in a program lets a user play a game and returns the score as an integer. you need to read a file 'hiscore.txt' which is either blank or contains the privious hi-score you need to write a program to update the hi-score whenever game() breaks the hi-score
'''def game():
    return 555

score = game()
with open("hiscore.txt") as f:
    hiscore=int(f.read())
    
if hiscore<score:
    with open("hiscore.text", "w") as f:
        f.write(str(score))'''

#4 a file contains a word "donkey" multiple times you need to write program to replace the word with #### by updating the same file
'''with open("ganesh.txt") as f:
     content= f.read()

content=content.replace("donkey", "#####")  
with open("ganesh.txt", "w") as f:
    f.write(content)  '''
#5 Repeat program for a lsit of such words to be censored
'''words =["donkey", "kaddu", "moti"]
with open("ganesh.txt") as f:
     content= f.read()
for word in words:
     content=content.replace( word, "#####")  
     with open("ganesh.txt", "w") as f:
      f.write(content)'''
#6write a program to mine a log file and find out whether it contains 'python'
'''with open("log.txt") as f:
     content = f.read()

if 'python' in content: # if you are checking for all type of python lower and upper case both you have put just" content.lower()"
     print("yes python is present.")  
else :
     print("python is not present.")   '''  

#7write a program to mine a log file and find out whether it contains 'python' in which line number?
'''content= True
i = 1
with open("log.txt") as f:
   
   while content:
       i+=1
       content = f.readline()

       if 'python' in content: # if you are checking for all type of python lower and upper case both you have put just" content.lower()"
        print(content)
        print(f"yes python is present in line number {i}.")  
        print(i)'''

#8---> write a program to create to make a copy of a text file "this.txt"
'''with open("this.txt") as f:
     content = f.read()

with open("copy.txt", 'w') as f:
     f.write(content) '''

#9--->write a program to find out whether a file is identical &  matches the content to another file or not
'''file1= "log.txt"
file2= "this.txt"
with open(file1) as f:
     f1= f.read()
with open(file2) as f:
     f2 = f.read()

if f1 == f2:
     print("files are identical.")     
else:
     print("files are not identical")  '''

#10---> write a program to wipe out all the contents  of a file using python  
'''with open('copy.txt', 'w') as f:
     f.write("") '''
#11---> wrrite a program to rename a file as "renamed_by_python.txt"
import os
oldname= "another2.txt"
newname="renamed_by_python.txt"
with open(oldname) as f:
     content=f.read()

with open(newname, 'w') as f:
     f.write(content)

os.remove(oldname)




