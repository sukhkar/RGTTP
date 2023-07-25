"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

def show_person_details(name: str, age: int) -> str:
    return "His/Her name is {} and he/she is {} years old".format(name, age)
    
print(show_person_details("Sukhendu", 29))
# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.



# 3. Show different representations of an integer.

# INSERT YOUR CODE HERE

# 4. Format a floating-point number with fixed precision.

floating_number = 34.45678

def show_precision(number: float) -> str:
    return "{:.3f}".format(number)

print(show_precision(floating_number))

# INSERT YOUR CODE HERE
