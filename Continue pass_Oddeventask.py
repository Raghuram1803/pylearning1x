#pass : to skip code

#ex:
#for i in range(1,10):
 #   pass
"""
for i in range(1,10):
    if i == 5: #if it is 5 it will skip
        pass
    else:
        print(i)
"""

# continue : skip values divisible by 3

for i in range (1,10):
    if i%2 == 0:
        print("even number found",i)
        continue
    print("odd number",i)