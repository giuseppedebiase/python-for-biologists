'''
The file input.txt contains a number of DNA sequences, one per line. Each sequence 
starts with the same 14 base pair fragment – a sequencing adapter that should have
been removed. Write a program that will (a) trim this adapter and write the cleaned 
sequences to a new file and (b) print the length of each sequence to the screen. 
'''

genomic = open("genomic_dna.txt")
# genomic_content stores the complete genomic sequence
genomic_content = genomic.read()
genomic.close()
# exons stores the start and end postion of every exon 
exons = open("exons.txt")

#coding_sequence is the output file with just the CDS
coding_sequence = open("coding_sequence.txt", "w")

for line in exons:
    # converts the line in the exons.txt file into a list
    position_list = line.split(",")
    # position_list[0] and [1] are type str so I had to typecast them to int for the string slicing on line 18
    start_p = int(position_list[0])
    end_p = int(position_list[1])
    print(start_p)
    coding_sequence.write(genomic_content[start_p:end_p] + "\n")

exons.close()
coding_sequence.close()
