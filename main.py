# =========================
# STEP 1: CREATE VARIABLES
# =========================

# Store the employee's first name
first_name = 'John'

# Store the employee's last name
last_name = 'Doe'

# These print statements were used for testing
# print(first_name)  # Output: John
# print(last_name)   # Output: Doe


# ===============================
# STEP 2: CONCATENATE FIRST/LAST NAME
# ===============================

# Combine first and last name directly
# Note: There is no space between the names yet
full_name = first_name + last_name

# print(full_name)  # Output: JohnDoe


# ===============================
# STEP 3: ADD SPACE BETWEEN NAMES
# ===============================

# Concatenate first and last name with a space in between
full_name = first_name + ' ' + last_name

# print(full_name)  # Output: John Doe


# =========================
# STEP 4: CREATE ADDRESS
# =========================

# Store a street address in a variable
address = '123 Main Street'

# print(address)  # Output: 123 Main Street


# =========================
# STEP 5: UPDATE ADDRESS
# =========================

# Append apartment information to the existing address
# += means "add and assign"
address += ', Apartment 4B'

# print(address)  # Output: 123 Main Street, Apartment 4B


# =========================
# STEP 6: REMOVE TEST PRINTS
# =========================

# Previous print() statements were commented out
# to keep the console output cleaner


# =========================
# STEP 7: EMPLOYEE DETAILS
# =========================

# Store the employee's age
employee_age = 28

# Store the employee's years of experience
experience_years = 5


# ==================================
# BUILD EMPLOYEE INFORMATION STRINGS
# ==================================

# Create a sentence describing the employee
# str() converts numbers into strings for concatenation
employee_info = full_name + ' is ' + str(employee_age) + ' years old'

# Display the employee information
print(employee_info)


# Create a string describing work experience
experience_info = 'Experience: ' + str(experience_years) + ' years'

# Display the experience information
print(experience_info)


# ==================================
# CREATE AN EMPLOYEE CARD
# ==================================

# Use an f-string for cleaner string formatting
employee_card = f'Employee: {full_name} | Age: {employee_age}'


# ==================================
# UPDATE EMPLOYEE CARD DETAILS
# ==================================

# Store the employee's position
position = 'Data Analyst'

# Store the employee's salary
salary = 75000

# Create a more detailed employee card
# f-strings allow variables to be inserted directly into strings
employee_card = (
    f'Employee: {full_name} | '
    f'Age: {employee_age} | '
    f'Position: {position} | '
    f'Salary: ${salary}'
)

# Display the updated employee card
print(employee_card)


# =========================
# STRING SLICING SECTION
# =========================

# Employee code format:
# DEV-2026-JD-001
employee_code = 'DEV-2026-JD-001'


# Extract the department code
# Starts at index 0 and stops before index 3
department = employee_code[0:3]

# Output: DEV
print(department)


# Extract the year code
# Starts at index 4 and stops before index 8
year_code = employee_code[4:8]

# Output: 2026
print(year_code)


# Extract the employee initials
# Starts at index 9 and stops before index 11
initials = employee_code[9:11]

# Output: JD
print(initials)


# Extract the last three characters
# Negative indexing counts from the end of the string
last_three = employee_code[-3:]

# Output: 001
print(last_three)
