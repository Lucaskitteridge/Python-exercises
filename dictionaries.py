#more or less same as js obejcts

#no doubles for keys

month_conversions = {
  "Jan" : "January",
  "Feb": "Febuary",
  "Mar": "March",
  "Apr" : "April"
}

print(month_conversions["Jan"])

#.get can have a default if not found as a second parameter
print(month_conversions.get("Luv", "Not a valid Key"))