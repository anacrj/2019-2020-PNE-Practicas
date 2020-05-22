from Seq1 import Seq
print("---Exercise 9---")
FOLDER = "../Session-04/"
FILENAME = "U5.txt"

s = Seq()
sequence = s.read_fasta(FOLDER + FILENAME)

print(f"Sequence: (Length: {s.len()}) {sequence}")
print(f"  Bases: {s.count()}")
print(f"  Reverse: {s.seq_reverse()}")
print(f"  Complement: {s.complement()}")
