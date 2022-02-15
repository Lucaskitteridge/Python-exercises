#appending to file
employee_file = open("employees.txt", "a")
#\n for newline
employee_file.write("\nKelly - Customer Service")
employee_file.close()

#w will overwrite the entire file or write a file that doesn't exist to make a new file
employee_file = open("employees1.txt", "w")
#\n for newline
employee_file.write("\nKelly - Customer Service")
employee_file.close()