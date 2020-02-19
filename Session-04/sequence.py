from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()
seq_dna = file_contents
index_finish = seq_dna.find("\n")
seq_dna = seq_dna[index_finish + 1:]
seq_dna = seq_dna.replace("\n", "")
length_sequence = len(seq_dna)

print(length_sequence)

# -- El resultado me da 33948 y no 33912 porque hay un comentario añadido en ADA, si lo quito me da bien
