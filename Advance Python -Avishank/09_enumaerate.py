list1=[3,53,5.2,False,"Ganesh"]
#method->1
'''index =0
for item in list1:
    print(item,index)
    index=index+1'''
#method->2
for index, item in enumerate(list1):
    print(index, item)
    