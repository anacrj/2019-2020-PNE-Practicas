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
def seq_count





