def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not good!,Ganesh")


a = increment('5dfdd')
print(a)
