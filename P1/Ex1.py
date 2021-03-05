from Seq1 import Seq

print("-----| Exercise 1 |------")
seq1 = Seq("ACTGA")

def print_seqs(sequence):
    print("Sequence 1: ( length:",  str(sequence.len()), ")", str(sequence))

print_seqs(seq1)