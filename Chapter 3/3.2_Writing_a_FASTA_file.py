'''
Write a program that will create a FASTA file for the following three sequences –
make sure that all sequences are in upper case and only contain the bases A, T, G 
and C.

Sequence header | DNA sequence
ABC123          | ATCGTACGATCGATCGATCGCTAGACGTATCG 
DEF456          | actgatcgacgatcgatcgatcacgact
HIJ789          | ACTGAC-ACTGT--ACTGTA----CATGTG
'''

FASTA_file = open("sequences.fasta", "w")
FASTA_file.write(">ABC123\nATCGTACGATCGATCGATCGCTAGACGTATCG\n")
FASTA_file.write(">DEF456\nactgatcgacgatcgatcgatcacgact\n")
FASTA_file.write(">HIJ789\nACTGAC-ACTGT--ACTGTA----CATGTG")
FASTA_file.close()
