"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

print(
    '''
    ==========================================
    |                 OUTPUT                 |
    ==========================================
    '''
)

print("PROBLEM:1\n---------")

def show_string():
  print("{} is a {} message with {} formatted {}".format("This", "test", "empty", "strings"))

show_string()

print("\n")

# INSERT YOUR CODE HERE

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

print("PROBLEM:2\n---------")
sentence = "Don't Panic!"

def show_sentence(sentence: str):
  print("{0}".format(sentence))

show_sentence(sentence)

print("\n")
# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

print("PROBLEM:3\n---------")
name: str = "Python"
adjective: str = "Great!!!"

def show_format_sentence(name: str, adjective: str):
  print("{name} is really {what}".format(name=name, what=adjective))

show_format_sentence(name, adjective)
