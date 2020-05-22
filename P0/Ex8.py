from Seq0 import *
FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"
FILENAME2 = "ADA.txt"
FILENAME3 = "FRAT1.txt"
FILENAME4 = "FXN.txt"

list_genes = [FILENAME1, FILENAME2, FILENAME3, FILENAME4]
bases = ["A", "C", "T", "G"]

print("---Exercise 8---")

for gene in list_genes:
    seq = seq_read_fasta(FOLDER + gene)
    dictionary = seq_count(seq)
    minimum = 0  # Se establece para que se quede con el valor mínimo
    maximum = ""
    for base, value in dictionary.items():
        while value > minimum:
            minimum = value
            maximum = base
    print("Gene", gene, ": Most frequent Base: ", maximum)
