from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

FOLDER = "../Session-04/"
FILENAME = "FRAT1.txt"

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080
# -- Create a client object
c = Client(IP, PORT)
# -- Print the IP and PORTs
print(c)

s = Seq().read_fasta(FOLDER + FILENAME)
Bases = str(s)
print(f"Gene {FILENAME}: {Bases}")
length = 10    # Length of fragments

c.talk(f"Sending {FILENAME} Gene to the server, in fragments of {length} bases...")

for i in range(5):
    fragment = Bases[i * length: (i + 1) * length]

    print(f"Fragment {i + 1}: {fragment}")
    c.talk(f"Fragment {i + 1}: {fragment}")

# First we have to launch the Teacher's server of Session-08 (server.py). Then execute the EX3.py program.
