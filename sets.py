import math
sample=set()
sample.add(1)
sample.add('Pluto')
sample.add(math.pi)
print(sample)
sample.add(math.pi)
print(sample)
# len command gives the number of elements of a set
print(len(sample))
sample.remove(math.pi)
print(sample)
# discard method can be also use as alternative to remove method

example2=set([2,5,2.3,'Elma'])
print(example2)
# .clear() method removes all elements from the set

#union and intersection of a set


odds=set([1,3,5,7,9])
evens=set([2,4,6,8,10])
primes=set([2,3,5,7])
composites=set([4,6,8,9,10])
print(odds.union(evens))
print(odds.intersection(primes))
print(odds.difference(primes))
# one can determine the existence of an element in a set with "in" and "not in"
print(2 in primes)
print(4 not in primes)
##############################################################################
# Python sets
# 1. Write a Python program to create a non empty set and print it.
sampleSet=set([2,3,12,3,math.pi])
print(sampleSet)
# 2. Write a Python program to add member in a set.
sampleSet.add('mega')
print(sampleSet)
# 3. Write a Python program to remove item from set.
sampleSet.discard('mega')
print(sampleSet)
# Python sets
# 4. Write a Python program to find the length of a set.
print(len(sampleSet))
# 5. Write a Python program to find maximum and the minimum
# value in a set.
print(min(sampleSet))
print(max(sampleSet))
# 6. Write a Python program to create an intersection of sets.
sampleSet2={3,4,5,'melon'}
print(sampleSet.intersection(sampleSet2))





