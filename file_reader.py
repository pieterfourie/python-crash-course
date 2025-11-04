from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text().strip()

print(contents)

print("\n")

pi_string = ''
for line in contents:
    pi_string += line.strip()

print(pi_string)
print('\n')
print(len(pi_string))
