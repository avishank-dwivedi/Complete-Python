#1---->Wrtite a program to open three files file1.txt,file2.txt and file3.txt . If any of these are not present, amessage without existing the program must be promting same..
def readFile(filename):
    try: 
        with open (filename,"r") as f:
         print(f.read())
    except FileNotFoundError :
       print(f"File{filename} is not found!")     
 
readFile("1.txt")        
readFile("2.txt")        
readFile("3.txt")        