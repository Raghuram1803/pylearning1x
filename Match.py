#match : similar to switch in java

"""""
name = input("enter your name\n")
match name:
     case "Raghu":
         print("Welcome raghu")
     case "munda":
         print("welcome munda")
     case _:
         print("welcome, there")
"""


#find week of the day

Day = int(input("enter the number 1-7 to know week of the day\n"))
match Day:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("invalid input")