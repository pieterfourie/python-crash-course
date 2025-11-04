from pathlib import Path

path = Path('text_files/programming.txt')
path.write_text("I love programming in Python!\nPython is my favorite language.")

# Python can only write strings to a file; if you want to write numbers,
# you need to convert them to strings first.

contents = "I love going to the gym and staying fit.\n"
contents += "Fitness is a lifestyle choice..\n"
contents += "Consistency is key to success.\n"

path.write_text(contents)

# If the file allready exists, the previous content is erased with write_text()