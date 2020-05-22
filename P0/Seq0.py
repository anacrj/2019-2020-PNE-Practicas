from pathlib import Path

# Exercise 1: seq_ping
def seq_ping():
    print("OK!")

# Exercise 2: seq_read_fasta()
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    f = file_contents.split("\n")
    chain = "\n".join(f[1:])
    return chain

# Exercise 3: seq_len()
def seq_len(filename):
    return len(filename)

# Exercise 4: seq_count_base()
def seq_count_base(seq, base):
    return seq.count(base)

# Exercise 5: seq_count()
def seq_count(seq):
    dictionary = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
                  'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return dictionary

# Exercise 6: seq_reverse()
def seq_reverse(seq):
    return seq[::-1]

# Exercise 7: seq_complement()
def seq_complement(seq):
    dict_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
    seq_comp = ""
    for base in seq:
        seq_comp = seq_comp + dict_bases[base]
    return seq_comp








