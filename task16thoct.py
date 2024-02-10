#write a program that calculates and displays the letter grade for a given numericals score based on following gradingscale
#A: 90-100, B: 80-89, c: 70-79, D: 60-69, E:0-59

score =int(input("Enter score to get grade\n"))
if score in list(range(90,100)):
    print("Grade is A")
elif score in list(range(80,89)):
    print("Grade is B")
elif score in list(range(70,79)):
    print("Grade is C")
elif score in list(range(60,69)):
    print("Grade is D")
elif score in list(range(0,59)):
    print("Grade is E")