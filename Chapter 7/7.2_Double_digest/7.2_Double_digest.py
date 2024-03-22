# In the chapter_7 file inside the exercises download, there's a file called dna.txt
# which contains a made-up DNA sequence. Predict the fragment lengths that we will
# get if we digest the sequence with two made-up restriction enzymes – AbcI, whose 
# recognition site is ANT*AAT, and AbcII, whose recognition site is GCRW*TG 
# (asterisks indicate the position of the cut site).

#N means any nucleotide, R is A or G, W is A or T

import re
file = open("dna.txt")
sequence = file.read()

#cuts is a list that will contain all the position of the cuts along the initial DNA sequence (counting from 1) and the length of the sequence
cuts = [0]

#AbcI
#restriction site: ANT*AAT
sites_AbcI = re.finditer(r"A[ATGC]TAAT", sequence)

for match in sites_AbcI:
    # + 3 and not + 2, match.start gives the INDEX (starts from 0) of the first char of the match
    # but we want the position of the cut (basically the last base for each fragment) starting from 1 to obtain the length of the fragments
    start = match.start() + 3
    cuts.append(start)

#AbcII
#restriction site: GCRW*TG
sites_AbcII = re.finditer(r"GC(A|G)(A|T)TG", sequence)

for match in sites_AbcII:
    start = match.start() + 4
    cuts.append(start)

last_base_position = len(sequence) - 1
cuts.append(last_base_position)

fragments_number = len(cuts) - 1

#cuts contain the position of the restriction sites for both enzymes
cuts = sorted(cuts)

print("The fragments generated by the enzymatic digestion will have the following lengths:")
for i in range(fragments_number):
    #this loop prints the difference between each of the elements in the list and the number that precedes it
    print(str(cuts[i+1] - cuts[i]) + "nt")
