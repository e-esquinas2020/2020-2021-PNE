import Seq0

GENE = "U5.txt"
FOLDER = "../Session-04/"
U5_seq = Seq0.seq_read_fasta(FOLDER + GENE)
print("------|EXERCISE 6|------")
print("Frag: " + U5_seq[:20] + "\nRev: " + Seq0.seq_reverse(U5_seq[:20]))