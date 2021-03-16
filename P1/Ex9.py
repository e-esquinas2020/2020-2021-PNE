from Seq1 import Seq

def print_result( sequence):
    print("Sequence: ( length:", str(sequence.len()), ")", str(sequence), "\n"
          , "BASES:", str(sequence.seq_count()), "\n"
          , "REV:", str(sequence.seq_reverse()), "\n"
          , "COMP:", str(sequence.seq_complement()))

print("-----| Exercise 9 |------")
s1 = Seq()
s1.seq_read_fasta("U5.txt")

print_result(s1)