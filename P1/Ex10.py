from Seq1 import Seq

gene_list=["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

def print_result(list):
    for gene in list:
        sequence = (Seq.seq_read_fasta(str(gene) + ".txt")).seq_count()
        value_list = list(sequence.values())
        print("Gene", gene, ": Most frequent Base:", max(value_list)[1])

print("-----| Exercise 10 |------")

print_result(gene_list)