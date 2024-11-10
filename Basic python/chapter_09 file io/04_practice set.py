#1--->write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'twinkle'
'''f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present.")
else:
    print("twinkle is not present.") 

f.close() '''

#2---->the game() function in a program lets a user play a game and returns the score as an integer. you need to read a file 'hiscore.txt' which is either blank or contains the privious hi-score you need to write a program to update the hi-score whenever game() breaks the hi-score
def game ():
     return 64

score =game()
'''def game():
    return 455

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
#6write a program to mine a log file and find out whether it contains 'python' words



