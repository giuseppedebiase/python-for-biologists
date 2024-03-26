# Write a program that will translate a DNA sequence into protein. Your program 
# should use the standard genetic code which can be found at this URL
# https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=tgencodes#SG1

import re

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

start_codon = 0
end_codon = 3

DNA_sequence = 'ACGATCGATCGTNACGTACGATCGTACTCGTAG'
protein_sequence = ''
k = len(DNA_sequence)

while end_codon <= k:
    codon = DNA_sequence[start_codon:end_codon]
    if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        break
    elif 'N' in codon:
        protein_sequence += 'X'
        start_codon += 3
        end_codon += 3
    else:
        protein_sequence += (translation(codon))
        start_codon += 3
        end_codon += 3

print(protein_sequence)