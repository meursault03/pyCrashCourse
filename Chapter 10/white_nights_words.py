from pathlib import Path

white_nights_file = Path('white_nights.txt').read_text(encoding='utf-8')

print(white_nights_file.lower().count("the "))

