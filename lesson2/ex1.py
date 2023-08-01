"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

print(
    '''
    ==========================================
    |                 OUTPUT                 |
    ==========================================
    '''
)

print("PROBLEM:1\n---------")

name: str = "Sukhendu"
age: int = 29

def show_person_details(name: str, age: int) -> str:
    return f"His/Her name is {name} and he/she is {age} years old."
    
print(show_person_details(name, age))

print("\n")
# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

print("PROBLEM:2\n---------")
version = 17.2
codename = "spymaster"

def show_padding(code: str, ver: int):
    print("Left Padding:{:<20} - {}".format(code, ver))
    print("Right Padding:{:>19} - {}".format(code, ver))
    print("Centre Padding:{:^18} - {}".format(code, ver))

show_padding(codename, version)

print("\n")
# 3. Show different representations of an integer.

print("PROBLEM:3\n---------")
number = 100

def int_represent(number: int):
    print("The number {} in binary format is : {:#b}".format(number, number))
    print("The number {} in decimal format is : {:#d}".format(number, number))
    print("The number {} in octal format is : {:#o}".format(number, number))
    print("The number {} in hexdecimal format is : {:#x}".format(number, number))
    print("The number {} in Hexdecimal format is : {:#X}".format(number, number))
    print("The number {} in number format is : {:#n}".format(number, number))

int_represent(number)

print("\n")
# 4. Format a floating-point number with fixed precision.

print("PROBLEM:4\n---------")
floating_number = 34.45678

def show_precision(number: float) -> str:
    return "{:.3f}".format(number)

print(show_precision(floating_number))