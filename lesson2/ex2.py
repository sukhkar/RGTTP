"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

def show_string():
  print("{0} is a {1} message with {2} formatted {3}".format("This","test","empty", "strings"))

show_string()

# INSERT YOUR CODE HERE

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

sentence = "Don't Panic!"

def show_sentence(sentence: str):
  print("{0}".format(sentence))

show_sentence(sentence)

# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

def show_format_sentence():
  print("{name} is really {what}".format(name="This", what="great"))

show_format_sentence()
