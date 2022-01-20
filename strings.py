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

my_string = "This is MY string!"
print(my_string[0:4]) # From the start till before the 4th index
print(my_string[1:7])
print(my_string[8:len(my_string)]) # From the 8th index till the end

print(my_string[0:7:2])  # A step of 2 meaning every second letter in that slice
print(my_string[0:7:5])  # A step of 5
print(my_string[::-1])  # The whole string in reverse (step is -1)

