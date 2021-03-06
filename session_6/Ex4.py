from session_6.Seq01 import print_seqs, generate_seqs
import termcolor

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
text1 = print_seqs(seq_list1)
termcolor.cprint(text1, "green")

print()
print("List 2:")
print_seqs(seq_list2)