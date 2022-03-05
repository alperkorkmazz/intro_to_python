import sys
tuple_1=(1,3,5,2,34,5)
list_1=[1,3,5,2,34,5]
print(80*"x")
print(tuple_1)
# tuples have less methods if one compare with Lists, but they are faster
print(dir(tuple_1))
print(dir(list_1))
# Lists occupy more memory
#print(dir(sys))
#print(help(sys.getsizeof()))
print("Tuple Size=",sys.getsizeof(tuple_1))
print("List size=",sys.getsizeof(list_1))
# Lists have add, remove, change methods but tuples can not be changed