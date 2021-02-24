def count_dna(seq):
    count_a, count_g, count_c, count_t = 0, 0, 0, 0
    for e in seq:
        if e.lower == "a":
            count_a += 1
        elif e.lower == "g":
            count_g += 1
        elif str(e).lower == "t":
            count_t += 1
        elif str(e).lower == "c":
            count_c += 1
    return count_a, count_g, count_c, count_t

def read_file(filename):
    with open(filename, 'r') as f:
        dna = f.read()
        dna = dna.replace("\n","")
        return dna
seq = read_file("dna.txt")
a, g, c, t = count_dna(seq)
print("TOTAL COUNT: ", (a+g+t+c), "A: ", a, "G: ", g, "C: ", c, "T: ", t)