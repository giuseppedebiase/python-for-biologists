# Write a program that will translate a DNA sequence into protein. Your program 
# should use the standard genetic code which can be found at this URL
# https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1

import re

#The codons that code for the same aa will often start with the same two letters so I used regex (which are not present in the solution presented in the book) to make the dict smaller
codons = {
    'F' : r'TT(T|C)',
    'L' : r'(TT(A|G)|CT[TCAG])',
    'S' : r'(TC[TCAG]|AG(T|C))',
    'Y' : r'TA(T|C)',
    'C' : r'TG(T|C)',
    'W' : r'TGG',
    'P' : r'CC[TCAG]',
    'H' : r'CA(T|C)',
    'Q' : r'CA(A|G)',
    'R' : r'(CG[TCAG]|AG(A|G))',
    'I' : r'AT[TCA]',
    'M' : r'ATG',
    'T' : r'AC[TCAG]',
    'N' : r'AA(T|C)',
    'K' : r'AA(A|G)',
    'V' : r'GT[TCAG]',
    'A' : r'GC[TCAG]',
    'D' : r'GA(T|C)',
    'E' : r'GA(A|G)',
    'G' : r'GG[TCAG]'
}

def translation(c):
    for aa, codon in codons.items():
        found = re.finditer(codon, c)
        for match in found:
            return aa

#values of the first and the third base of each codon (starting with the first)
start_codon = 0
end_codon = 3

DNA_sequence = 'ACGATCGATCGTNACGTACGATCGTACTCGTAG'
protein_sequence = ''
k = len(DNA_sequence)

#The while loop stop when the value of end_codon exceeds the length of the DNA sequence
while end_codon <= k:
    codon = DNA_sequence[start_codon:end_codon]
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        #TAA, TAG and TGA are the stop codons
        break
    elif 'N' in codon:
        #for the codons that contain the letter N the translated aa will be an X
        protein_sequence += 'X'
        start_codon += 3
        end_codon += 3
    else:
        protein_sequence += (translation(codon))
        start_codon += 3
        end_codon += 3

print(protein_sequence)
