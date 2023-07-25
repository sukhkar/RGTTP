"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

dict_variable = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

def show_dict_key_values(shared_dict: dict):
    for _ in shared_dict:
        print("Key : {} and Value : {}".format(_,shared_dict[_]))

show_dict_key_values(dict_variable)

# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE

# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE
