"""
  Lesson 2: ex3.py
"""

print(
    '''
    ==========================================
    |                 OUTPUT                 |
    ==========================================
    '''
)

print("PROBLEM:1\n---------")

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

person = ["Sukhendu", 29, "Engineer"]

def show_person(person_info: list) -> str:
    return "He/She is {} and his/her age is {}. He/She is working as {}." \
            .format(person_info[0], person_info[1], person_info[2])

print(show_person(person))
print("\n")

# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

print("PROBLEM:2\n---------")

book_details = {"title": "Python-Fundamentals", "author": "Robin", "publication_year": 2023}

def show_book(book: dict) -> str:
    return "The guidebook {0} by {1} was published in {2}." \
            .format(book['title'], book['author'], book['publication_year'])

print(show_book(book_details))

print("\n")
# INSERT YOUR CODE HERE

# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

print("PROBLEM:3\n---------")
spaceship_details = {"name": "Curiosity", "type": "car-sized Mars rover", "purpose": "Laboratory mission"}

def show_spaceship(spaceship: dict) -> str:
    return "The spaceship is called the {name}. It is a {type} used for {purpose}." \
            .format(name=spaceship['name'], type=spaceship['type'], purpose=spaceship['purpose'])

print(show_spaceship(spaceship_details))
