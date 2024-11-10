#LIST COMPREHENSIONS:---->
'''
it is an elegant way to create lists based on existiing list.
'''

a =[3,6,7,8,9,2,4,23,75,23,123,67]
#method-> 1
'''b = []
for item in a:
    if item%2==0:
        b.append(item)

print(b) '''
#Shortcut to print the same output.  
#method->2
b = [i for i in a if i%2==0]     
print(b)
