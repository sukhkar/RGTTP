"""
  Lesson 5: ex3.py
"""

from typing import Any

# 1. Write a for loop to iterate over list: [1, 2, 3, 'a', 'b', 'c']

combine_list: list[Any] = [1, 2, 3, 'a', 'b', 'c']

for _ in combine_list:
    print(_)

# 2. Write for loop to print each character in word "orange"

fruit: str = "orange"

for _ in fruit:
    print(_)

# 3. Using following shopping list:
# shopping_list: ['orange', 'banana', 'mandarin']
# Print "Note to self, buy: " and then iterate
# over each element in the list

shopping_list: list[str] = ['orange', 'banana', 'mandarin']
print("Note to self, buy: ")
for _ in shopping_list:
    print(_)

# 4. Write for loop using range to print numbers from 0 to 10

for _ in range(11):
    print(_)

# 5. Write for loop using range to print numbers from 10 to 20

for _ in range(10, 21):
    print(_)

# 6. Write for loop using range to print even numbers from 10 to 20

for _ in range(10, 21):
    if _ % 2 == 0:
        print(_)

# 7. Write for loop using range, to print every 5 numbers
#    down from 100 to 0

for _ in range(100, 0, -5):
    print(_)

# 8. Write for loop using enumerate to print element and it's index

for _ in enumerate(shopping_list):
    print("Index : {} and Item : {}".format(_[0], _[1]))
