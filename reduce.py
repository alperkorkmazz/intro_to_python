# reduction for nested values - reduces the work with the iterable collections
# Data: [a_1,a_2,...,a_n]
# Function: f(x,y)
# reduce(f,data):
# Step 1: val_1=f(a_1,a_2)
# Step 2: val_2=f(val_1,a_3)
# Step 3: val_3=f(val_2,a_4)
# Step n-1: val_n-1=f(val_n-2,a_n)
# return val_n-1
from functools import reduce
#multiply all numbers in a list
data=[2,3,4,6.4,7,9,6.7,5.6,3]
multiplier=lambda x,y:x*y
print(reduce(multiplier,data))

