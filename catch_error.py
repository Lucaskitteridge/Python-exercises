try:
  value = 10/0
  number = int(input("Enter number "))
  print(number)
except ZeroDivisionError as err:
  print(err)
except ValueError:
  print("invalid input")

#like an if statement or a catch in way. If theres an error in above code then the except activates
#can specify the type of error and to run a catch based on the error type.
#can assign errors to a variable with as