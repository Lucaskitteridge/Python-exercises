# lists/ arrays are same as Js as with accessing indexes

freinds = ["Morley", "Sophie", "Kevin", "Josh", "Sophie"]
lucky_numbers = [7, 13, 22, 66, 999]

# freinds.extend(lucky_numbers) #concats arrays together

freinds.append("John")

# first parameter is the index to add, and the second is the value

freinds.insert(1, "Susan")
freinds.remove("Kevin")  # value to remove

# freinds.clear() #emptys array

freinds.pop()  # remove last element

print(freinds.index("Morley"))

# count amout of times the value appears in list

print(freinds.count("Sophie"))
freinds.sort()
freinds2 = freinds.copy()
print(freinds2)
