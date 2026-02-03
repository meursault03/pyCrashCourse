from pathlib import Path

cat_file = Path('cats.txt')
dog_file = Path('dogs.txt')

def read_and_print(file_path):
     """Read a file and print its contents line by line."""
     try:
         path = file_path.read_text().title()
     except FileNotFoundError:
         print(f"Sorry, the file {file_path} does not exist.")
     else:
         print(path)

read_and_print(cat_file)
read_and_print(dog_file)

