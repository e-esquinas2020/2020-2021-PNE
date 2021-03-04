import termcolor
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        if Seq.is_valid_sequence_2(strbases):
        #or if Seq0.is_valid_sequence(strbases): (importing)
            print("New sequence created!")
            self.strbases = strbases
        else:
            self.strbases = "Error!"
            print("INCORRECT Sequence detected")
        #will work because the class has been established once the sequence has been instanciated

    def is_valid_sequence(self):
        for b in self.strbases:
            if b != "A" and b != "C" and b != "T" and b != "G":
                return False
        return True

    #if we use this we don't need self as an argument
    @staticmethod
    def is_valid_sequence_2(bases):
        for b in bases:
            if b != "A" and b != "C" and b != "T" and b != "G":
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
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
        #for j in range(0, len(pattern)):
    return list_seq

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    def __init__(self, strbases, name):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        if self.is_valid_sequence():
            """Print the Gene name along with the sequence"""
            return self.name + "-" + self.strbases
        else:
            return "Not a gene"

# --- Main program
#s1 = Seq("AGTACACTGGT")
#g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
#print(f"Sequence 1: {s1}")
#print(f"  Length: {s1.len()}")
#print(f"Gene: {g}")
#print(f"  Length: {g.len()}")
