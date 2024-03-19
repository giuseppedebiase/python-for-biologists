# Use the data from the previous exercise, but instead of creating a single FASTA file, 
# create three new FASTA files – one per sequence. The names of the FASTA files 
# should be the same as the sequence header names, with the extension .fasta.

#first FASTA
sequence_one = open("ABC123.fasta", "w")
sequence_one.write(">ABC123\nATCGTACGATCGATCGATCGCTAGACGTATCG")
sequence_one.close()

#second FASTA
sequence_two = open("DEF456.fasta", "w")
sequence_two.write(">DEF456\nactgatcgacgatcgatcgatcacgact")
sequence_two.close()

#third FASTA
sequence_three = open("HIJ789.fasta", "w")
sequence_three.write(">HIJ789\nACTGAC-ACTGT--ACTGTA----CATGTG")
sequence_three.close()
