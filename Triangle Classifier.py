#Write a program that classifies a triangle based on its side lengths.
"'"
#Given three input values representing the lengths of the sides, determine if the triangle is
#equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal)
side1 = input("Enter value of side1\n")
side2 = input("Enter value of side2\n")
side3 = input("Enter value of side3\n")
if side1==side2==side3:
    print("Its equilateral triangle")
elif (side1==side2 or side1==side3 or side2==side3):
    print("Its isoceles triange")
elif(side1!=side2 or side1!=side3 or side2!=side3):
    print("its scalar triangle")