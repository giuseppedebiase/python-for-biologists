# Here's a short section of genomic DNA:
# ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
# It comprises two exons and an intron. The first exon runs from the start of the 
# sequence to the sixty-third character, and the second exon runs from the ninety-
# first character to the end of the sequence. Write a program that will print just the
# coding regions of the DNA sequence. 

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
p1 = 63
p2 = 91
# with string slicing the end value is not included, so the end string will end with character 62 (if you start counting from 0)
# or value 63 is yous tart counting from 1
exon1 = my_dna[0:p1]
# with string slicing the beginning character is included, if I used 91 as p1 the resulting string would've started
# with the 92nd character (counting from 0) so I subtracted 1 from 91 to have a substring that begins from 
# the 90th character (counting from 0) ot the 91st character (counting from 1)
exon2 = my_dna[p2-1:len(my_dna)]
print(exon1 + exon2)
