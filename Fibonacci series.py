#The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones.
#It typically starts with 0 and 1.
#So, the Fibonacci series begins: 0, 1, 1, 2, 3, 5, 8, 13 and so on.

"""""
num = int(input("Enter a number\n"))
a,b = 0,1
for i in range(num):
    print(a,end=" ")
    a,b = b, a+b
"""
a,b=0,1
while a<10:
    print(a,end=" ")
    a,b = b,a+b