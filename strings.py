# use \ for special characters

string = 'This isn\'t flying, this is falling with style!'
print(string)

#indexes are similar to js

c = "cats"[0]
n = "Ryan"[1]

print(c, n)

#examples of string methods

parrot = "Norwegian Blue"
print(len(parrot)) #length
print(parrot.lower()) #lowercase
print(parrot.upper()) #uppercase
print(str(14)) #number to string

# dot notation only works with strings but () words with other types

string_1 = "Camelot"
string_2 = "place"

# %s as a replacement and a % after string to signift end. Like a psql query

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))