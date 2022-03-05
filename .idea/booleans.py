a=2
b=4
a==b
# type(False)
print(type(False))
# 0 -> False, all other positive or negative numbers are True
# Empty string "" is False the other Strings are always True when they are converted
# to boolean with bool("sads"), or bool(""),
# trivial values are False, nontrivial values are True
# str(True)-> 'True' (toString), str(False) -> 'False'
print(type((str(True))))
# int(True), int(False)
print(int(True))
print(int(False))
print(5+True) # 6
print(10*False) #0
print(False*1)
# Terminalde dir() mevcut kullanilabilirleri verir
# dir(__buildins__)