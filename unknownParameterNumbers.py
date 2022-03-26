# degisken sayisi bilinmedigi durumlarda fonksiyonlar tanimlanabilir
# parameter arg verildiginde fonksiyon icinde calisilabilir

def Sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(Sum(1,3,4,2,1))
print(Sum(1,3,))
print(Sum(1,2,2,4))
print(Sum())