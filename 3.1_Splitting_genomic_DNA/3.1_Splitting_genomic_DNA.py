# Look in the chapter_3 folder for a file called genomic_dna.txt – it contains the same 
# piece of genomic DNA that we were using in the final exercise from chapter 2. Write
# a program that will split the genomic DNA into coding and non-coding parts, and 
# write these sequences to two separate files. 
# Hint: use your solution to the last exercise from chapter 2 as a starting point.
# Solution for the last exercise of chapter 2: https://github.com/giuseppedebiase/python-for-biologists/blob/main/2.6_Splicing_out_introns_3.py
p1 = 62
p2 = 91
my_file = open("genomic_dna.txt")
sequence = my_file.read()
print(sequence)
exon1 = sequence[0:p1]
exon2 = sequence[p2-1:len(sequence)]
intron1 = sequence[p1:p2-1]

coding_sequence = open("coding.txt", "w")
coding_sequence.write(exon1 + exon2)
coding_sequence.close()

noncoding_sequence = open("noncoding.txt", "w")
noncoding_sequence.write(intron1)
noncoding_sequence.close()
