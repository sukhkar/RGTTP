"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Add banana to a shopping list.

shopping_list.append('banana')

# 2. Add chocolate in the third position in your shopping list

shopping_list.insert(3, 'chocolate')

# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

new_shopping_list: list[str] = ['chocolate', 'carrot', 'avocado']

shopping_list.extend(new_shopping_list)

# 4. Remove first chocolate only

index: int = shopping_list.index('chocolate')

shopping_list.pop(index)

# 5. Remove last item from the list

shopping_list.pop()

# 6. Remove third item from the list

shopping_list.pop(2)

# 7. Count how many carrots are in the shopping list?

number_carrots: int = shopping_list.count('carrot')

print("There are {} {} in the shopping list".format(number_carrots, 'carrot'))

# 8. Get the index of the chocolate (careful can throw traceback)

try:
    choco_index = shopping_list.index('chocolate')
    print("Chocolate is in {} postion in shopping list...!!!".
          format(choco_index))
except ValueError as e:
    print(e)

# 9. Get the index of carrot, make sure this code is executed

item: str = "apples"
item = 0


def find_item_index(item: str) -> list:
    index_item: list = []
    for i in range(len(shopping_list)):
        if shopping_list[i] == item:
            index_item.append(i)
    return index_item


indices: list[int] = find_item_index(item)
if indices:
    print("{} present in indices {}".format(item, indices))
else:
    print("{} not in shopping list".format(item))
