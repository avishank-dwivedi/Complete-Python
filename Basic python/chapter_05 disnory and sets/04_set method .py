# creating a empty set
b = set()
print(type(b))
#Adding values in empty set
b.add(4)
b.add(5)
b.add(5)#adding a value repetedly dose not change the sets
# b.add([4,5,6]) it will  throws an error also cannot add dictionary e.g- {4:5}

print(b)
#sets are unorder and unindex............
# b.remove(5)
# print(len(b)) print the lenth of set 

print(b.pop())
'''set.clear
set.intersection
set.union '''
s1 = {1, "ganesh", True, 44, 4}
s1.add("hello")
print(s1)




