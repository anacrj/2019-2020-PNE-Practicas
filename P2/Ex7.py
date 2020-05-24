from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

FOLDER = "../Session-04/"
FILENAME = "FRAT1.txt"
# -- Create the client objects
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
# -- Print the IP and PORTs
print(c1)
print(c2)

s = Seq().read_fasta(FOLDER + FILENAME)
Bases = str(s)
length = 10

print(f"Gene {FILENAME}: {Bases}")
mes = f"Sending {FILENAME} Gene to the server, in fragments of {length} bases..."

c1.talk(mes)
c2.talk(mes)

for i in range(10):
    fragment = Bases[i * length: (i+1) * length]
    print(f"Fragment {i+1}: {fragment}")
    mes2 = f"Fragment {i+1}: {fragment}"
    if i % 2:
        c2.talk(mes2)
    else:
        c1.talk(mes)

