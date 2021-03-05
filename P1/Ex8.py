from Seq1 import Seq

print("-----| Exercise 7 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_seq = [s1, s2, s3]

for i in range(0, len(list_seq)):
    print("Sequence", str(i), ": ( length:",  str(list_seq[i].len()), ")", str(list_seq[i]), "\n"
      , "BASES:", str(list_seq[i].seq_count()), "\n"
      , "REV:", str(list_seq[i].seq_reverse()), "\n"
      , "COMP:", str(list_seq[i].seq_complement()))