"""
  Lesson 4: ex2.py
"""

# 1. Create 'fruits' dictionary and add following key: values
# apple: 10
# orange: 2
# banana: 3

fruits: dict[str, int] = {"apple": 10, "orange": 2, "banana": 3}

print(f"List of Fruits: {fruits}")

# 2. Iterate over fruits in fruits dictionary using for loop,
#    print using f-strings:
#    apple: 10
#    orange: 2
#    banana: 3

for fruit in fruits:
    print(f"{fruit}: {fruits[fruit]}")

# 2. Iterate over the keys in 'fruits' dictionary

for key in fruits.keys():
    print(f"Fruit item : {key}")

# 3. Iterate over the values in dictionary

for value in fruits.values():
    print(f"Number of Fruit item : {value}")

# 4. Access value banana using .get() method

print("NUmber of Banana in fruit list : ", fruits.get("banana"))

# 5. Access value mandarin using .get() method,
#    if 'mandarin' doesn't exist, return 0

mandarin: int = 0

if "mandarin" in fruits:
    mandarin = fruits.get("mandarin")

print("Number of Mandarin in fruits :", mandarin)

# 6. Remove all items from the dictionary

fruits.clear()

print(f"Removed all the items from Fruits: {fruits}")
