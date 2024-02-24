square = [1, 4, 9, 16, 25]
print(square[0])
print(square[-1])

#check if list is empty
list2 = []
if not list: #not will check if list is empty
    print("empty list")
else:
    print("Not empty")

#pop: removes and return, remove the value not the index
square = [1, 4, 9, 16, 25]
print(square.pop(1))
print(square)

print("-------------------------------------")

#type conversions
st = "raghuram"
out = list(st)
print(out)