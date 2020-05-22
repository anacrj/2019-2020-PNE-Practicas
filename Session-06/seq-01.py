class Seq:
    """"A class for representing sequence objects"""

    def __init__(self, strbases):  # esto se usa para iniciar el object
        self.strbases = strbases  # Initialize the sequence with the value passed as argument when creating the object
        print("New sequence created!")

    def __str__(self):  # Method called when the object is being printed
        return self.strbases  # We just return the string with the sequence

    def len(self):      # Calculate the length of the sequence
        return len(self.strbases)


class Gene(Seq):
    pass  # con esto indicamos que no hay nada en ese class


# -- Main program
s1 = Seq("AACGTC")
g = Gene("ACCGTA")
# s2 = Seq("CCGTCGA")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {g}")
print(f"The length of the sequence 1 is {s1.len()}")
print(f"The length of the sequence 2 is {g.len()}")

# -- print ("Testing objects...")
