seq_DNA = input("Introduce the sequence of DNA: ")
A = 0
C = 0
T = 0
G = 0
for letter in seq_DNA:
    if letter == "A":
        A = A + 1
    elif letter == "C":
        C = C + 1
    elif letter == "T":
        T = T + 1
    elif letter == "G":
        G = G + 1
total_length = A + C + T + G
print("The total length of the sequence is: ", total_length)
print("A: ", A)
print("C: ", C)
print("T: ", T)
print("G: ", G)
