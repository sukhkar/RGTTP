"""
  Lesson 4: ex3.py
"""

from collections import defaultdict
from typing import Any

# 1. Create dictionary using comprehension
# {key, value = i, i**2}

num_squr: dict[int, int] = {i: i**2 for i in range(10)}

print("Dict comprehension of number and it's Square", num_squr)

# 2. Create another comprehension and add +1 to each key's value.
# {key, value = i, i+1}

num_dict: dict[int, int] = {i: i+1 for i in range(10)}

print("Dict comprehension of number and it's corresponding value", num_dict)

# 3. Create 'fruits' defaultdict():
# apple: 10
# orange: 2
# banana: 3
# and for any other key set it's default value to 0


def default():
    return 0


fruits: dict[str, int] = {"apple": 10, "orange": 2, "banana": 3}

fruits_dict: defaultdict[Any, Any] = defaultdict(default)

# 4. Sort the 'fruits' dictionary using sorted() method
# by keys and values, dictionary does not have .sort()

print("Sorted the Fruits dictionary by it's Keys : ",
      dict(sorted(fruits.items())))

# 5. Return 'sorted_fruits' dictionary using sorted() method,
# sort by values.


def sort_by_value(item):
    return item[1]


sorted_fruits: dict[str, int] = dict(sorted(fruits.items(), key=sort_by_value))

print("Sorted the Fruits dictionary by it's values : ", sorted_fruits)

# 6. Reverse the 'sorted_fruits' dictionary and print the dictionary.

reversed_fruits: dict[str, int] = dict(sorted(fruits.items(),
                                              key=sort_by_value, reverse=True))

print("Reversed the sorted fruits dictionary by it's values : ",
      reversed_fruits)
