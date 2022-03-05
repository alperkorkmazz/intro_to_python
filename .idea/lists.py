sampleList=[1,3,4,5,6,56]
print(sampleList)
sampleList.append(3.4)
sampleList.append(3.5)
print(sampleList[0])
# last item index is -1
print(sampleList[-1])
#slicing -> beginning value included end index not
print(sampleList[2:5])
sampleList2=[128,True,'Alpha',1.34,[2,3,4]]
print(sampleList2)
#lists can be concatenation by + operator
print(sampleList+sampleList2)
print(sampleList2+sampleList)
# reverse order?
sampleList2.reverse()
print(sampleList2)
for o in reversed(sampleList2):
    print(o)

list3 = [3,2,5,6,7,0]
list3.reverse()
print(list3)
list3.sort()
print(list3)