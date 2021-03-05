from pathlib import Path
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            print("NULL sequence created")
            self.strbases = strbases
        else:
            if Seq.valid_sequence_2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = "Error!"
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
        if self.strbases == "NULL" or self.strbases == "Error!":
            return 0
        else:
            return len(self.strbases)

    def take_out_first_line(self, seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def seq_read_fasta(self, filename):
        #sequence = Path(filename).read_text()
        sequence = take_out_first_line(Path(filename).read_text())
        return sequence

    def count_base(self, base):
        return self.strbases.count(base)


    def seq_count(self):
        gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        if self.strbases == "NULL" or self.strbases == "Error!":
            return gene_dict
        else:
            for d in self.strbases:
                gene_dict[d] += 1
            return gene_dict

    def seq_reverse(self):
        if self.strbases == "NULL" or self.strbases == "Error!":
            return self.strbases
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        gene_dict = {"A": "T", "C": "G", "G": "C", "T": "A"}
        comp_str = ""
        if self.strbases == "NULL" or self.strbases == "Error!":
            return self.strbases
        else:
            for b in self.strbases:
               comp_str += gene_dict[b]
            return comp_str