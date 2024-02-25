#set = a set is an unordered collection of data types that is iterable, mutable and has no duplicate elements
set1 = set() #empty set
print(set1)

set2 = set("Raghu")
print(set2)

set3 = {1,2,3,4,5,5,4} #if multiple duplicate also then it will remove
print(set3)

t = ("Raghu","is","Raghu","learning")
s = set(t)
print(s)

#union
u1 = {1,2,3,4,7}
u2 = {4,6,7}
uni = u2.union(u1)
print(uni)
unii = u2.intersection(u1)
print(unii)
unidif = u1.difference(u2)
print(unidif)

#subset : If one is part of other or not
subset1 = {1,2,3,4,5}
subset2 = {2,3,4,6}
subset = set1.issubset(set2)
print(subset)