from pathlib import Path

def seq_ping():
    print("OK")

def take_out_first_line(seq):
    return seq[seq.find("\n")+1:].replace("\n", "")

def seq_read_fasta(filename):
    #sequence = Path(filename).read_text()
    sequence= take_out_first_line(Path(filename).read_text())
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    a, c, t, g = 0,0,0,0
    for d in seq:
        if d == "A":
            a += 1
        elif d== "C":
            c += 1
        elif d== "T":
            t += 1
        elif d== "G":
            g+= 1
    return {"A": a, "C": c, "G": g, "T": t}
#or we could do:
    #gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    #for d in seq:
    #   gene_dict[d] += 1
    #return gene_dict

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    gene_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
    comp_str = ""
    for b in seq:
       comp_str += gene_dict[b]
    return comp_str
