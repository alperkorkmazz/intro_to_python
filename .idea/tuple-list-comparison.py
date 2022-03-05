import timeit
list_test=timeit.timeit(stmt="[1,2,3,4,5]", number=10000000)
tuple_test=timeit.timeit(stmt="(1,2,3,4,5)", number=10000000)
print(list_test)
print(tuple_test)

empty_t=()
tuple_1=("a",) # without comma, python converts it to string
tuple_2=("a")
tuple_3=("a","b")
print(empty_t)
print(tuple_1)
print(tuple_2)
print(tuple_3)
# Tuples can be defined without paranthesis
empty_t1=()
tuple_11="a", # without comma, python converts it to string
tuple_21="a"
tuple_31="a","b"
print(empty_t1)
print(tuple_11)
print(tuple_21)
print(tuple_31)
print(type(tuple_11))

# Tuple elements have also indexes
info=("John", 27, "Germany", True)
print("Name=", info[0])
print("Age=", info[1])
print("Country=", info[2])
print("Married=", info[3])
print(90*"+")
info2=("John", 27, "Germany", True)
name,age,country,married=info2 # number of variables must be equal to the number of tuple elements
print("Name=", name)
print("Age=", age)
print("Country=", country)
print("Married=", married)

