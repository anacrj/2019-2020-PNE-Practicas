import socket

import termcolor
from Seq1 import Seq

IP = "127.0.0.1"
PORT = 8080

seq_get = ["ACTGAACTTGACCTACGGTCA","TTCGACCGGAAGTCCAATTTG","CCTAGGAACTTTGACGTAACT","ACGTCAGCTAGTGCTAACGTA","ATTGCTAAGGTTCTGAGTACT"]

FOLDER = "../Session-04/"
FILENAME1 = "U5.txt"
FILENAME2 = "ADA.txt"
FILENAME3 = "FRAT1.txt"
FILENAME4 = "FXN.txt"
FILENAME5 = "RNU6_269P.txt"
list_genes = [FILENAME1, FILENAME2, FILENAME3, FILENAME4, FILENAME5]


# --- 1) Step 1: Creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- 2) Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- 3) Step 3: Convert into a listening socket
ls.listen()


def get_function(n):
    return seq_get[n]


def info_function(strseq):
    s = Seq(strseq)
    l = s.len()
    ac = s.count_base("A")
    tc = s.count_base("T")
    cc = s.count_base("C")
    gc = s.count_base("G")
    response = f"""Sequence: {s}
    Total length: {l}
    A: {ac} ({round((ac/l)*100)})%  
    C: {cc} ({round((cc/l)*100)})%     
    T: {tc} ({round((tc/l)*100)})%     
    G: {gc} ({round((gc/l)*100)})%"""
    return response


def complement_function(strseq):
    s = Seq(strseq)            # Create the object sequence from the string
    return s.complement()


def reverse_function(strseq):
    s = Seq(strseq)            # Create the object sequence from the string
    return s.seq_reverse()


def gene_function(name):
    s = Seq()
    s.read_fasta(FOLDER + name)
    return str(s)


print("Server is configured!")


while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        req_raw = cs.recv(2000)
        req = req_raw.decode()
        lines = req.split("\n")             # Remove the \n
        line0 = lines[0].strip()
        lfunct = line0.split(' ')                 # Separate the line into command an argument

        function = lfunct[0]                           # The first element is the command

        try:
            arg = lfunct[1]
        except IndexError:
            arg = ""
        response = ""

        if function == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!"
        elif function == "GET":
            termcolor.cprint("GET", 'green')
            response = get_function(int(arg))
        elif function == "INFO":
            termcolor.cprint("INFO", 'green')
            response = info_function(arg)
        elif function == "COMP":
            termcolor.cprint("COMP", 'green')
            response = complement_function(arg)
        elif function == "REV":
            termcolor.cprint("REV", 'green')
            response = reverse_function(arg)
        elif function == "GENE":
            termcolor.cprint("GENE", 'green')
            response = gene_function(arg)
        else:
            termcolor.cprint("Unknown command!!!", 'red')
            response = "Unkwnown command"

        # Send the response message
        response = response + '\n'
        print(response)
        cs.send(response.encode())
        cs.close()
