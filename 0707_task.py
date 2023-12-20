#Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

#Task1
r = int(input("Enter radius to calculate area of circle\n"))
Pie = 3.14
#print(type(Pie))
area = Pie*(r**2)
print(area)
print("-------task 1 Done--------------------")

#Task2
#Create a program that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second number

n1 = int(input("Enter number1\n"))
n2 = int(input("Enter number2\n"))
print(n1>n2)
print(n1<n2)
print(n1==n2)
print(n1 if n1>n2 else n2)

print("--------task 2 Done-------------")

#task3 Develop a Python script that calculates the square and cube of a given numbe
n3 = int(input("Enter value to calculate square and cube of number\n"))
print("Square of",n3,"is",n3**2)
print("Cubeof",n3,"is", n3**3)
