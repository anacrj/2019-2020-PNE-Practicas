from Seq1 import Seq
s = Seq()
print("---Exercise 10---")

FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"
FILENAME2 = "ADA.txt"
FILENAME3 = "FRAT1.txt"
FILENAME4 = "FXN.txt"
FILENAME5 = "RNU6_269P.txt"

list_genes = [FILENAME1, FILENAME2, FILENAME3, FILENAME4, FILENAME5]
bases = ["A", "C", "T", "G"]

for gene in list_genes:
    seq = s.read_fasta(FOLDER + gene)
    dictionary = s.count()
    minimum = 0  # Se establece para que se quede con el valor mínimo
    maximum = ""
    for base, value in dictionary.items():
        while value > minimum:
            minimum = value
            maximum = base
    print("Gene", gene, ": Most frequent Base: ", maximum)
