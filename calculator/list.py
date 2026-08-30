list1 = [1,2,3,4,5]
list2=[]
while list1:
    list2.append(list1.pop())
list2.reverse()
print(list2)