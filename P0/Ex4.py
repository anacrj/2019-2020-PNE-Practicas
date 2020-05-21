from Seq0 import *
FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"
FILENAME2 = "ADA.txt"
FILENAME3 = "FRAT1.txt"
FILENAME4 = "FXN.txt"

list_genes = [FILENAME1, FILENAME2, FILENAME3, FILENAME4]
bases = ["A", "C", "T", "G"]

print("---Exercise 4---")

for element in list_genes:
    seq = seq_read_fasta(FOLDER + element)
    print("Gene:", element)
    for letter in bases:
        print(letter, ":", seq_count_base(seq, letter))
