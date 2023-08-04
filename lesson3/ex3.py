"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

sorted_shopping_list: list[str] = sorted(shopping_list)

print(sorted_shopping_list)

# 2. Sort the list using .sort() method and print that list

shopping_list.sort()

print(shopping_list)

# 3. Use the built-in function reversed(), reverse the list and print that list

# The return type of reversed method is a iterator object
reversed_shopping_list: list[str] = reversed(shopping_list)

# Converted the iterator object to a list and then print the same
print(list(reversed_shopping_list))

# 4. Reverse the list using sort() method and print the list

shopping_list.sort(reverse=True)

print(shopping_list)

# 5. Reverse the list using sorted() method and print the list

reverse_shopping_list: list[str] = sorted(shopping_list, reverse=True)

print(reverse_shopping_list)