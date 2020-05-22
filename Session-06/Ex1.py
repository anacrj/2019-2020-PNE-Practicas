class Seq:
    """"A class for representing sequence objects"""

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


# -- Main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
