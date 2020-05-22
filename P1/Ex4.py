from Seq1 import Seq
print("---Exercise 4---")
sequence1 = Seq()                      # Create a Null sequence
sequence2 = Seq("ACTGA")               # Create a valid sequence
sequence3 = Seq("Invalid sequence")    # Create an invalid sequence

print(f"Sequence 1: (Length: {sequence1.len()}) {sequence1}")
print(f"Sequence 1: (Length: {sequence2.len()}) {sequence2}")
print(f"Sequence 1: (Length: {sequence3.len()}) {sequence3}")
