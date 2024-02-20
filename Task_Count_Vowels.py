#aeiou in string and print how many
string = input("enter a sentence\n")
vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count = count +1
print(count)

