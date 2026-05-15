# Employee Information & String Manipulation Project 🧑‍💼🐍

A beginner-friendly Python project that demonstrates the fundamentals of string manipulation, variable handling, concatenation, f-strings, and string slicing.

This project simulates a simple employee information system where employee details are created, updated, and formatted using Python.

---

## 📖 Project Overview

This program introduces essential Python concepts through practical examples such as:

* Creating variables
* Concatenating strings
* Updating variables
* Formatting output with f-strings
* Converting integers to strings
* Extracting parts of strings using slicing

The project is ideal for beginners learning Python fundamentals and preparing for backend development concepts.

---

## 🧠 Concepts Practiced

### ✅ Variables

The project stores employee information in variables such as:

```python
first_name = 'John'
last_name = 'Doe'
employee_age = 28
```

---

### ✅ String Concatenation

Combining strings together using the `+` operator:

```python
full_name = first_name + ' ' + last_name
```

Output:

```python
John Doe
```

---

### ✅ Updating Variables

Appending additional information to existing strings:

```python
address += ', Apartment 4B'
```

---

### ✅ Type Conversion

Using `str()` to convert numbers into strings before concatenation:

```python
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
```

---

### ✅ f-Strings

Using formatted string literals for cleaner and more readable code:

```python
employee_card = f'Employee: {full_name} | Age: {employee_age}'
```

---

### ✅ String Slicing

Extracting parts of strings using index positions:

```python
department = employee_code[0:3]
```

Output:

```python
DEV
```

---

## 📂 Full Program

```python
# Store employee information
first_name = 'John'
last_name = 'Doe'

# Combine names
full_name = first_name + ' ' + last_name

# Store and update address
address = '123 Main Street'
address += ', Apartment 4B'

# Employee details
employee_age = 28
experience_years = 5

# Create employee information
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

# Experience details
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Employee card
position = 'Data Analyst'
salary = 75000

employee_card = (
    f'Employee: {full_name} | '
    f'Age: {employee_age} | '
    f'Position: {position} | '
    f'Salary: ${salary}'
)

print(employee_card)

# String slicing
employee_code = 'DEV-2026-JD-001'

department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]

print(department)
print(year_code)
print(initials)
print(last_three)
```

---

## ▶️ Example Output

```python
John Doe is 28 years old
Experience: 5 years
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
DEV
2026
JD
001
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

* Python syntax
* Variable assignment
* String concatenation
* f-strings
* Data formatting
* String indexing and slicing
* Output formatting
* Basic backend programming logic

---

## 🛠 Technologies Used

* Python 3

---

## 🚀 How to Run the Project

### Clone the Repository

```bash id="k4m2yx"
git clone https://github.com/ikwukao/employee_string_project.git
```

### Navigate Into the Project Folder

```bash
cd employee-string-project
```

### Run the Program

```bash
python main.py
```

---

## 📚 Ideal For

* Python beginners
* freeCodeCamp learners
* Backend engineering practice
* String manipulation practice
* Students learning programming fundamentals

---

## 🔥 Skills Demonstrated

* Clean Python syntax
* Problem solving
* String manipulation
* Data formatting
* Beginner backend logic
* Readable and maintainable code

---

## 📄 License

This project is open-source and free to use for educational purposes.

## Program Output

![Employee Profile Generator program output](./img/employee_profile_generator.png)
---
