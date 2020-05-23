from pathlib import Path


class Seq:

    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            self.strbases = "NULL"
            print("NULL Sequence created")
            return
        bases = ["A", "T", "C", "G"]
        for element in strbases:
            if element not in bases:
                self.strbases = "ERROR"
                print("Invalid Sequence!")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):  # Method called when the object is being printed
        return self.strbases

    def len(self):      # Calculate the length of the sequence
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def count(self):
        dictionary = {'A': self.count_base('A'), 'T': self.count_base('T'),
                      'C': self.count_base('C'), 'G': self.count_base('G')}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return "A:", 0, "T:", 0, "C:", 0, "G:", 0
        return dictionary

    def seq_reverse(self):
        if self.strbases == "NULL":
            return self.strbases
        elif self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == "NULL":
            return self.strbases
        elif self.strbases == "ERROR":
            return self.strbases

        dictionary = {"A": "T", "T": "A", "C": "G", "G": "C"}
        comp_sequence = ""
        for element in self.strbases:
            comp_sequence = comp_sequence + dictionary[element]
        return comp_sequence

    def perc (self,base):
        return round((float(self.count(base))/float(self.len())) * 100, 1)

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        body = file_contents.split('\n')[1:]         # Remove the head
        self.strbases = "".join(body)                # Store the sequence read from the file
        return self
