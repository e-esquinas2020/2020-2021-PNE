import Seq0

GENE = "U5.txt"
FOLDER = "../Session-04/"
U5_seq = Seq0.seq_read_fasta(FOLDER + GENE)
print("------|EXERCISE 7|------")
print("Frag: " + U5_seq[:20] + "\nComp: " + Seq0.seq_complement(U5_seq[:20]))