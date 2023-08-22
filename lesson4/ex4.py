"""
  Lesson 4: ex4.py
"""

# 1. Create a data variable which contains a list of objects
#    with following key and values:
#    {"category": "fruit", "name": "apple"}
#    {"category": "fruit", "name": "banana"}
#    {"category": "fruit", "name": "orange"}
#    {"category": "vegetable", "name": "carrot"}
#
#    Write a for loop to print out the fruits and vegetables.

data = [
    {"category": "fruit", "name": "apple"},
    {"category": "fruit", "name": "banana"},
    {"category": "fruit", "name": "orange"},
    {"category": "vegetable", "name": "carrot"}
]

object_dict: dict[str, list[str]] = {}

for value in data:
    if value["category"] in object_dict:
        object_dict[value.get("category")].append(value.get("name"))
    else:
        object_dict[value.get("category")] = [value.get("name")]

print("List of ruits and vegetables : ", object_dict)
