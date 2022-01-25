is_male = True
is_tall = True

#indent for if statement as well

#or is js equivalent of ||
#and is js equivalent of &&

if is_male and is_tall:
  print("You are a male or tall or both")
else:
  print("You are not a male or not tall or both")

  #elif fo else if

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3