from pathlib import Path
import json


def dump(dumped_data, path):
    """
        Serializes a Python object to JSON and writes it to a file.

        Parameters:
            dumped_data (Any): The data to save (dict, list, int, etc.).
            path (str): The filename or path where data should be stored.

        Returns:
            int: The number of characters written to the file.
        """
    place = Path(path)
    content = json.dumps(dumped_data)
    return int(place.write_text(content))

def read_dump(path):
    """
        Reads a JSON file from disk and converts it back into a Python object.

        Parameters:
            path (str): The filename to read from.

        Returns:
            Any: The Python object (list, dict, etc.) loaded from the JSON data.
        """
    place = Path(path)
    content = json.loads(place.read_text())
    return print(f"Your favorite number is {content}")

def ask_fav_number():
    favorite_number = int(input("What's your favorite number? "))
    return favorite_number


try:
    read_dump("favorite_number.json")
except FileNotFoundError:
    fav_number = ask_fav_number()
    dump(fav_number,"favorite_number.json")
    print("We will get your favorite number next time")

