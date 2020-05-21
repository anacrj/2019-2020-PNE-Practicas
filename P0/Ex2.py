from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"

DNA_FILE = FOLDER + FILENAME

sequence = seq_read_fasta(DNA_FILE)
print("DNA_FILE: ", FILENAME)
print("The first 20 bases are:", sequence[:20])
