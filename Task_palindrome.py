"""""
Task #1 Palindrome Checker:
Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
Example -
madam - reverse(madam) -> same
Naman -> reverse -> same
Malayalam
Compare String with the Revserse of the string
"""


#user_input= input("Enter the input string")
#logic: if you reverse and match with old string. It should be same

#def reverse_string(input_string):
#    reverse_str = ""
#    for char in input_string:
#        reverse_str = char + reverse_str
#    return reverse_str


#original_str = "mam"
#rev_str = reverse_string(original_str)
#print(rev_str)

#if original_str == rev_str:
#    print("palindrome")
#else:
#    print("Not a palindrome")


#original_str = input("Enter a string\n")

#def palindrome(original_str):
 #reverse_str = original_str[::-1]
 #if original_str == reverse_str:
  #   print("palindrome")
 #else:
  #   print("Not a palindrome")

#palindrome(original_str)

orginal_string = "Raghuram"

def rev_string(orginal_string):
    return ''.join(reversed(orginal_string))

rev_str = rev_string(orginal_string)
print(rev_str)
