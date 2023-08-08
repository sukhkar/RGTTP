"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']

class ShoppingList:
    def __init__(self, shopping_list: list) -> object:
        self.shopping_list = shopping_list

# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.

    def in_list(self, item: str) -> bool:
        for i in self.shopping_list:
            if i == item:
                return "{} is in shopping list".format(item)
        return "{} not in shopping list".format(item)

# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']

    def show_shopping_list(self) -> str:
        return "My shopping list : {}".format(self.shopping_list)

# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False

    def obj_comparison(self, compare_obj: object) -> str:
        if self.shopping_list == compare_obj.shopping_list:
            return f"Both the list are identical : {self.shopping_list}"
        return "There is a difference between shopping list {} and {}".format(self.shopping_list, compare_obj.shopping_list)

# Create the shopping list object with list of items
shopping_obj: object = ShoppingList(['apples', 'milk', 'bread', 'carrot', 'pasta'])
other_shop_obj: object = ShoppingList(['apple', 'milk', 'bread', 'carrot', 'pasta'])

# Check if item present on shopping list
print(shopping_obj.in_list("apples"))

#Print the shopping list output
print(shopping_obj.show_shopping_list())

# Compare the shopping list object with another shopping list of object
print(shopping_obj.obj_comparison(other_shop_obj))