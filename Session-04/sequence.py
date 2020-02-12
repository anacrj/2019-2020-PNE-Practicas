from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
f = file_contents.split("\n")
chain = ''.join(f[1::])
letterA = "A"
letterT = "T"
letterC = "C"
letterG = "G"

print("Total:", chain.count(letterA) + chain.count(letterT) + chain.count(letterC) + chain.count(letterG))
