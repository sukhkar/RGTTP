"""
  Lesson 5: ex1.py
"""

from typing import Any

# 1. Create even() function that return "I am even!" if number is even
#    or "I am odd!" if the number is odd.

number: int = 10


def even(number: int) -> str:
    if number % 2 == 0:
        return "I am even!"
    else:
        return "I am odd!"


even(number)

# 2. Create safe_even() function, that will output "I am not number!" if
#    the input is not an number otherwise will work same as even()


def safe_even(any_input: Any) -> str:
    if type(any_input) is int:
        return even
    else:
        return "I am not number!"


safe_even("Test")

# 3. Create a function fizz_buzz(),
#    replacing any number divisible by three with the word "fizz",
#    and any number divisible by five with the word "buzz",
#    and any number divisible by both 3 and 5 with the word "fizzbuzz",
#    and number if number is not divisible by any.


def fizz_buzz(number: int) -> str:
    if type(number) != int:
        return "Not a valid Number"
    output_str: str = ""
    if number % 3 == 0:
        output_str += "fizz"
    if number % 5 == 0:
        output_str += "buzz"

    return output_str if output_str else number

# 4. Execute fizz_buzz() function from 1 to the 100


for i in range(100):
    print(fizz_buzz(i))
