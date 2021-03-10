from Seq1 import Seq # test_seq
#s1 = test_seq()

def print_result(i, list_seq):
    print("Sequence", str(i), ": ( length:", str(list_seq[i].len()), ")", str(list_seq[i]))
    print(list_seq[i].count_base())


print("-----| Exercise 6 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
#list_seq = [s1, s2, s3]

print("Sequence 1: ( length:",  str(s1.len()), ")", str(s1), "\n"
      , "BASES:", str(s1.seq_count()))
print("Sequence 2: ( length:",  str(s2.len()), ")", str(s2), "\n"
      , "BASES:", str(s2.seq_count()))
print("Sequence 3: ( length:",  str(s3.len()), ")", str(s3), "\n"
      , "BASES:", str(s3.seq_count()))
#for i in range(0, len(list_seq)):
      #print_result(i, list_seq[i])
