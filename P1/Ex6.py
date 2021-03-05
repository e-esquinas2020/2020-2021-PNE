from Seq1 import Seq

print("-----| Exercise 6 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

print("Sequence 1: ( length:",  str(s1.len()), ")", str(s1), "\n"
      , "BASES:", str(s1.seq_count()))
print("Sequence 2: ( length:",  str(s2.len()), ")", str(s2), "\n"
      , "BASES:", str(s2.seq_count()))
print("Sequence 3: ( length:",  str(s3.len()), ")", str(s3), "\n"
      , "BASES:", str(s3.seq_count()))