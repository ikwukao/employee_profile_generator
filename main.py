# Step 1

first_name = 'John'
last_name ='Doe'
# print(first_name) # Outputs: John
# print(last_name) # Outputs: Doe

# Step 2
full_name = first_name + last_name
# print(full_name) # Outputs: JohnDoe

# Step 3
full_name = first_name + ' ' + last_name
# print(full_name) # Outputs: John Doe

# Step 4
address = '123 Main Street'
# print(address) # Outputs: 123 Main Street

# Step 5
address += ', Apartment 4B'
# print(address) # Outputs: 123 Main Street, Apartment 4B

# Step 6
# Remove every `print()` statement from the code

# Step 7
employee_age = 28

# More interesting part
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

employee_card = f'Employee: {full_name} | Age: {employee_age}'
