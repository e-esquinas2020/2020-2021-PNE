import termcolor
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        if Seq.is_valid_sequence_2(strbases):
            print("New sequence created!")
            self.strbases = strbases
        else:
            self.strbases = "Error!"
            print("INCORRECT Sequence detected")

    def is_valid_sequence(self):
        for b in self.strbases:
            if b != "A" and b != "C" and b != "T" and b != "G":
                return False
        return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for b in bases:
            if b != "A" and b != "C" and b != "T" and b != "G":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

def print_seqs(list_sequences):
    for i in range(0, len(list_sequences)):
        text = "Sequence", str(i), ": length:",  str(list_sequences[i].len()), str(list_sequences[i])
        termcolor.cprint(text, "yellow")

def generate_seqs(pattern, number):
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq