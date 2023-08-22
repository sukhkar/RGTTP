"""
  Lesson 4: ex1.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2

fruits: dict[str, int] = {"apple": 10, "orange": 2}

print(f"List of Fruits: {fruits}")

# 2. Add banana to the dictionary and set it's value to 3

fruits["banana"] = 3

print(f"List of Fruits: {fruits}")

# 3. Add mandarin using dictionary method .update()

fruits.update({"mandarin": 10})

print(f"List of Fruits: {fruits}")

# 4. Remove the mandarin from the dictionary

del fruits["mandarin"]

print(f"List of Fruits: {fruits}")

# 5. Add 10 more apples and remove 2 bananas

fruits["apple"] += 10

fruits["banana"] -= 2

print(f"List of Fruits: {fruits}")

# 6. Remove 'apple' from the dictionary using .pop()
#    and save it's value into a variable 'apples'

fruits["apples"] = fruits.pop("apple")

print(f"List of Fruits: {fruits}")

# 7. Remove 'mandarin' from the dictionary using .pop()
#    and save it's value into a variable 'mandarin'
#    if 'mandarin' doesn't exist set the variable to 0

mandarin: int = 0

if "mandarin" in fruits.keys():
    mandarin = fruits.pop("mandarin")

print("Number of Mandarin in fruits :", mandarin)

# 8. Remove last item from the dictionary using .popitem()
#    and save it's value into variable 'last'

last: tuple = fruits.popitem()

print(f"List of Fruits: {fruits}")

# 9. Check if the 'banana' is in the fruits dictionary.

if "banana" in fruits.keys():
    print("Banana is there in fruits list")
else:
    print("Banana is not there in fruits list")
