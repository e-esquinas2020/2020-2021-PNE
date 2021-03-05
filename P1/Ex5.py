from Seq1 import Seq

print("-----| Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
list_seq = [s1, s2, s3]

for i in range(0, len(list_seq)):
    print("Sequence", str(i), ": ( length:",  str(list_seq[i].len()), ")", str(list_seq[i]), "\n"
      , "BASES: A :", str(list_seq[i]count_base("A")))
