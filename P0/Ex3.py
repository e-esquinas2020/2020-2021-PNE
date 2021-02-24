import Seq0

GENE_FOLDER = "../Session-04/"
gene_list=["U5", "ADA", "FRAT1"]

print("-----| Exercise 3 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("Gene", gene, "length:", Seq0.seq_len(sequence))