# Using the data from part one, write a program that will print out the original 
# genomic DNA sequence with coding bases in uppercase and non-coding bases in 
# lowercase. 
# Part 1: https://github.com/giuseppedebiase/python-for-biologists/blob/main/2.4_Splicing_out_introns_1.py

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
p1 = 62
p2 = 91
exon1 = my_dna[0:p1]
exon2 = my_dna[p2-1:len(my_dna)]
intron1 = my_dna[p1:p2-1]
print(exon1 + intron1.lower() + exon2)
