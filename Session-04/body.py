from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "U5.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
f = file_contents.split("\n")
chain = ''.join(f[1::])

# -- Print the contents on the console
print("The body of the U5.txt file is: ", chain)
