from Seq1 import Seq
#import Seq1
#llamamos a la funcion con Seq1.FUNCION()

def print_result(i, sequence):
    print("Sequence", str(i), ": ( length:",  str(sequence.len()), ")", str(sequence), "\n"
      , "BASES:", str(sequence.seq_count()), "\n"
      , "REV:", str(sequence.seq_reverse()))

print("-----| Exercise 7 |------")
s1 = Seq()
s12 = Seq()
s12.seq_read_fasta("U5.txt")
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_seq = [s1, s12, s2, s3]



for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])
