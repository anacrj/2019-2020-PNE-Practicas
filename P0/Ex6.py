from Seq0 import *
FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"
print("---Exercise 5---")
print("Gene ", FILENAME1, ":")
print("Frag:", seq_read_fasta(FOLDER + FILENAME1)[:20])
print("Rev:", seq_reverse(seq_read_fasta(FOLDER + FILENAME1)[:20]))