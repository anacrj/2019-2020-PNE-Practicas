class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):  # Method called when the object is being printed
        return self.strbases

    def len(self):      # Calculate the length of the sequence
        return len(self.strbases)


# -- Main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


def print_seqs(sequence):
    for seq in sequence:
        print(f"Sequence {sequence.index(seq)}: (Length: {seq.len()}) {seq}")


print_seqs(seq_list)
