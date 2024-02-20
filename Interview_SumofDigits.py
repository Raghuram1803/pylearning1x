#Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
#12345 = 1+2+3+4+5

#num = input("enter the digits to calculate sum\n")
#sum = 0
#digit = 12345
#mod = digit%10
#print(mod)

num = int(input("Enter your number\n"))
sum = 0
while num!=0:
    digit = num%10
    sum = sum + digit
    num = int(num/10)
print(sum)

