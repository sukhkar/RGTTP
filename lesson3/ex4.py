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


shopping_obj: object = ShoppingList(['apples', 'milk', 'bread', 'carrot', 'pasta'])

print(shopping_obj.in_list("apples"))
print(shopping_obj.show_shopping_list())