from Seq0 import *
FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"
FILENAME2 = "ADA.txt"
FILENAME3 = "FRAT1.txt"
FILENAME4 = "FXN.txt"

list_genes = [FILENAME1, FILENAME2, FILENAME3, FILENAME4]

print("---Exercise 3---")
for gene in list_genes:
    sequence = seq_read_fasta(FOLDER + gene)
    print(f"Gene {gene} ---> Length: {seq_len(sequence)}")
