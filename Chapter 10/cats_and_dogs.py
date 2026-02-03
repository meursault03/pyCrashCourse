from pathlib import Path

cat_file = Path('cats.txt')
dog_file = Path('dogs.txt')
vale_file = Path('vales.txt')

def read_and_print(file_path):
     """Read a file and print its contents line by line."""
     try:
         path = file_path.read_text().title()
     except FileNotFoundError:
         pass
     except NameError:
         print(f"No value found in variable")
     else:
         print(path)

read_and_print(cat_file)
read_and_print(dog_file)
read_and_print(vale_file)
