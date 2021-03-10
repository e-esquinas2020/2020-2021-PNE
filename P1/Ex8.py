from Seq1 import Seq

def print_result(i, sequence):
    print("Sequence", str(i), ": ( length:", str(sequence.len()), ")", str(sequence), "\n"
          , "BASES:", str(sequence.seq_count()), "\n"
          , "REV:", str(sequence.seq_reverse()), "\n"
          , "COMP:", str(sequence.seq_complement()))

print("-----| Exercise 8 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_seq = [s1, s2, s3]

for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])