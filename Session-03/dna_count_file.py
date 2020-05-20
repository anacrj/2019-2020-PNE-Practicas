A = 0
C = 0
T = 0
G = 0
with open('dna.txt', 'r') as f:
    for line in f:
        for letter in line:
            if letter == "A":
                A = A + 1
            elif letter == "C":
                C = C + 1
            elif letter == "T":
                T = T + 1
            elif letter == "G":
                G = G + 1
        total_length = A + C + T + G
    f.close()
print("The total length of the sequence is: ", total_length)
print("A: ", A)
print("C: ", C)
print("T: ", T)
print("G: ", G)
