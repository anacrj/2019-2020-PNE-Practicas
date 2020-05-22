from Seq0 import *
FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"

print("---Exercise 7---")

seq = seq_read_fasta(FOLDER + FILENAME1)

print("Gene ", FILENAME1, ":")
print("Frag:", seq[:20])
print("Comp:", seq_complement(seq[:20]))
