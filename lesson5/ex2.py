"""
  Lesson 5: ex2.py
"""

# 1. Write a while true loop to print "Forever" forever

while True:
    print("Forever")

# 2. Write a while loop to print numbers from 0 to 42

number: int = 0

while number <= 42:
    print(number)
    number += 1

# 3. Write a while true loop to print numbers from 0 to 42

number: int = 0

while True:
    print(number)
    number += 1
    if number > 42:
        break

# 4. Write a while true loop to print numbers from 0 to 45, and instead
#    of 42, print "I am 42!" break at number 45.

age: int = 42
number: int = 0

while True:
    print("I am 42!") if number == 42 else print(number)
    number += 1
    if number > 45:
        break

# 5. Write a while-else loop to count to 2, and after that print
#    "It's my turn now!" using else statement.

count: int = 0

while count <= 2:
    print(count)
    count += 1
else:
    print("It's my turn now!")
