from pathlib import Path
class Seq:
    """A class for representing sequences"""
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):
        if strbases == Seq.NULL_SEQUENCE :
            print("NULL sequence created")
            self.strbases = strbases
        else:
            if Seq.valid_sequence_2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print("INCORRECT Sequence detected")

    @staticmethod
    def valid_sequence_2(bases):
        for b in bases:
            if b != "A" and b != "C" and b != "T" and b != "G":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    @staticmethod #we are not using attrubutes of the class (like self.strbases), so its staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def seq_read_fasta(self, filename):
        #sequence = Path(filename).read_text()
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())
        return self.strbases

    def count_base(self):
        a, c, t, g = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, t, g
        for d in self.strbases:
            if d == "A":
                a += 1
            elif d == "C":
                c += 1
            elif d == "T":
                t += 1
            elif d == "G":
                g += 1
        return a, c, t, g


    def seq_count(self):
        gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return gene_dict
        else:
            for d in self.strbases:
                gene_dict[d] += 1
            return gene_dict
        #a, c, t, g= self.count_base()
        #return gene_dict = {"A": a, "C": c, "G": g, "T": t}


    def seq_reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return self.strbases
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        gene_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
        comp_str = ""
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return self.strbases
        else:
            for b in self.strbases:
               comp_str += gene_dict[b]
            return comp_str

    #def test_seq(self):
        #s1=
        #return s1