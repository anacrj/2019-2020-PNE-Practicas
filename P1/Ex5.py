from Seq1 import Seq
print("---Exercise 5---")
sequence1 = Seq()                      # Create a Null sequence
sequence2 = Seq("ACTGA")               # Create a valid sequence
sequence3 = Seq("Invalid sequence")    # Create an invalid sequence

bases = ["A", "G", "C", "T"]
list_seq = [sequence1, sequence2, sequence3]
for element in list_seq:
    print(f"Sequence {list_seq.index(element)}: (Length {element.len()}){element}")
    for b in bases:
        print(f"{b}: {element.count_base(b)}", end=", ")
    print("")
