import pathlib

pi = pathlib.Path('pi_digits.txt').read_text().splitlines()
pi_string = ""
for line in pi:
    pi_string += line.strip()

birthday = "676767" # DDMMYY format

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")



