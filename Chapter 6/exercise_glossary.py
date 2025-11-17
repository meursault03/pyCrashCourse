glossary = {
    "tuple": "It's like a fixed value list, the syntax is thistuple = ('apple','banana','cherry')",

    "list_comprehension": """Shorter syntax for creating a list with a for-each loop logic.
Example:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]""",

    "for_each": """A way to loop over (or 'iterate') every item in a collection. In Python, this is the standard 'for...in' loop.
Example:
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)""",

    "dictionary": """A mutable collection that stores data in key-value pairs. You use a unique key to access its value.
Example:
person = {"name": "Iuri Vale", "age": 25}
print(person["name"])  # Outputs 'Iuri Vale'""",

    "list_splitting": """Getting a 'slice' (a new list with a part of the original) using colon syntax: [start:end:step].
Example:
numbers = [0, 1, 2, 3, 4, 5]
sub_list = numbers[1:4]  # Gets [1, 2, 3]
first_half = numbers[:3] # Gets [0, 1, 2]
"""
}

for key, value in glossary.items():
    print(f"{key.title()}: {value}")