# tuple - It is immutable in nature - NO modification
girlfriends = ("D","N","New bee")
print(type(girlfriends))

#Merging tuple
girlfriends1 = ("I", "like", "Everyone")
overallgf = girlfriends + girlfriends1
print(overallgf)

#covert to list
convtolist = list(overallgf)
print(convtolist)

#search in tuples
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Tokyo" in cities)
