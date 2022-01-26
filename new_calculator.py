num1 = float(input("Enter first number "))
operator = input("Enter operator")
num2 = flaot(input("Enter second number "))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "/":
  print(num1 / num2)
elif operator == "*":
  print(num1 * num2)
else:
  print('not acceptable operator')