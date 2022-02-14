#first is file path, second is what we want to do. This case is read
#w means add to the file
#r+ is read and write
employee_file = open("employees.txt", "r")
#check to make sure file is readable

print(employee_file.readable())

#reads whole file
#print(employee_file.read())
#specifiy the line to read
#print(employee_file.readline())
#if I were to run it again it automatically reads the next line
#print(employee_file.readline())
#or we can more easily use readlines and specify how many lines by turning each line into an alement in an array
#print(employee_file.readlines()[0])
#we can even loop through to read every line
for employee in employee_file.readlines():
  print(employee)

#need to make sure we also close file
employee_file.close()