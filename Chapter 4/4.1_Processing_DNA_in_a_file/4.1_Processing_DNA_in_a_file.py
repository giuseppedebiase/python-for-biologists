'''
The file input.txt contains a number of DNA sequences, one per line. Each sequence 
starts with the same 14 base pair fragment – a sequencing adapter that should have
been removed. Write a program that will (a) trim this adapter and write the cleaned 
sequences to a new file and (b) print the length of each sequence to the screen.
'''

my_file = open("input.txt")
#trimmed.txt will contain the trimmed sequences
trimmed_sequences = open("trimmed.txt", "w")

for line in my_file:
    # writes the trimmed sequence into the new file
    trimmed_sequences.write(line[14:len(line)])
    # prints the trimmed sequence
    print(line[14:len(line)])

my_file.close()
trimmed_sequences.close()
