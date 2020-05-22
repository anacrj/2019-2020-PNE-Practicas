from Seq1 import Seq
print("---Exercise 7---")
sequence1 = Seq()                      # Create a Null sequence
sequence2 = Seq("ACTGA")               # Create a valid sequence
sequence3 = Seq("Invalid sequence")    # Create an invalid sequence

print(f"Sequence 1: (Length: {sequence1.len()}) {sequence1}")
print(f"  Bases: {sequence1.count()}")
print(f"Rev: {sequence1.seq_reverse()}")
print(f"Sequence 2: (Length: {sequence2.len()}) {sequence2}")
print(f"  Bases: {sequence2.count()}")
print(f"Rev: {sequence2.seq_reverse()}")
print(f"Sequence 3: (Length: {sequence3.len()}) {sequence3}")
print(f"  Bases: {sequence3.count()}")
print(f"Rev: {sequence3.seq_reverse()}")
