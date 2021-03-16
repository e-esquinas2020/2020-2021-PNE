#Which is the most frequent base in each gene?
import Seq0

GENE_FOLDER = "../Session-04/"
gene_list=["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 8 |------")
for gene in gene_list:
    seq = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    inverse = [(value, key) for key, value in Seq0.seq_count(seq).items()]
    print("Gene", gene, ": Most frequent Base:", max(inverse)[1])
