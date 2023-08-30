"""
  Lesson 5: ex4.py
"""

# 1. Write a function get_index() that returns the index of
#    a character in a string


def get_index(word: str, char: str) -> int:
    for _ in enumerate(word):
        if _[1] == char:
            return _[0]


get_index("Sukhendu", "h")

# 2. Write a function shout() that returns each word
#  capitalized with "!" and on it's own line.


def shout(sentence: str):
    for word in sentence.split(" "):
        print(word.upper()+"!")


shout("This is Sukhendu")

# 3. Write a function extract_longer() that extracts
#    words longer or equal to n-characters and return a list,
#    otherwise return False


def extract_longer(sentence: str, n: int) -> list | bool:
    list_word: list[str] = []
    for word in sentence.split(" "):
        if len(word) >= n:
            list_word.append(word)

    return list_word if list_word else False


extract_longer("This is Sukhendu", 3)
