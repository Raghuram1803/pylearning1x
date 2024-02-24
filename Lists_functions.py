 #list
my_list = [1, 2, 3, 0.1, 50, 4, 42]
my_list1 = [1, 2, "Raghu"]

print(my_list)
print(my_list1[2])

#changin an element
my_list1[2] = "raghuram"
print(my_list1)

#append() :adding in end
my_list1.append("is great")
print(my_list1)

#extend()
my_list1.extend(["like","atg"])
print(my_list1)

#insert()
my_list1.insert(1,"iam")
print(my_list1)

#remove ()
my_list1.remove(1)
print(my_list1)

#copy
my_list1_copy = my_list1.copy()
print(my_list1_copy)

#clear
my_list1_copy.clear()
print(my_list1_copy)

#sorting
my_list.sort()
print(my_list)

#reverse
my_list.reverse()
print(my_list)

#split
sentence = input("Enter a name to check if its palindrome\n")
conv_list = list(sentence)
finalcheck = conv_list[::-1]
print(finalcheck)
if conv_list == finalcheck:
    print("tada palindrome")
else:
    print("Nope not a palindrome")


