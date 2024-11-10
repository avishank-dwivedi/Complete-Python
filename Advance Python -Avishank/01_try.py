while(True):
    print("press q to quit")
    a = (input("enter a number: "))
    if a=='q':
        break
    try:
       print("Try.........")
       a =int(a)
       if a>6:
         print("You enter a number greater than 6.")
    except Exception as e:
       print(f"Your input resulted in an error {e}")
print("Thanks for visiting!")  