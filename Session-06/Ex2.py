class Seq:

    def __init__(self, strbases):
        bases = ["A", "T", "C", "G"]
        for element in strbases:
            if element not in bases:
                self.strbases = "ERROR"
                print("ERROR")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):  # Method called when the object is being printed
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(sequence):
    for seq in sequence:
        print("Sequence", sequence.index(seq), ":", "(Length:", seq.len(), ")", seq)


# -- Main program
seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
