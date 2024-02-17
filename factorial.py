#5!=5*4*3*2*1
number = int(input("enter a number\n"))
if number<0:
    print("factorial is not possible\n")
else:
    fact= 1
for i in range(1, number+1): #0 to len-1 =range
        fact = fact*i
print("factorail is", fact)