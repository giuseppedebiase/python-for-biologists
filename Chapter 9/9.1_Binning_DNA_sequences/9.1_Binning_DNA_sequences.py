'''
In the chapter_9 folder in the exercises download there is a collection of files with 
the extension .dna which contain DNA sequences of varying length, one per line. 
Use this set of files for both exercises. 
Binning DNA sequences
Write a program which creates nine new folders - one for sequences between 100
and 199 bases long, one for sequences between 200 and 299 bases long, etc. Write 
out each DNA sequence in the input files to a separate file in the appropriate folder.

I didn't use floor() from math module or max() since they are not present in the book
'''
import os

#this function gives back floor(n/100)
def floor_100(n):
    result = str(n/100)
    result = int(result[0:result.index('.')])
    return result

#dict with key: sequence and value:length of sequence
sequences = {}

for file in os.listdir('.'):
    if file.endswith('.dna'):
        file = open(file)
        for sequence in file:
            sequence= sequence.rstrip('\n')
            sequences[sequence] = len(sequence)

#number of ranges (bins) is the length of the longest sequence/100, rounded down
#example: longest seq is 255nt, bins are 2, 100-199 and 200-299
max_length = 0
for sequence, length in sequences.items():
    if length > max_length:
        max_length = length

n_ranges = floor_100(max_length)

#creates the folders for the various bins
for i in range(1, n_ranges + 1):
    start = str(i*100)
    end = str(i*100 + 99)
    os.mkdir(start + '-' + end)

#puts each sequence in the respective bin
i = 1
for sequence, length in sequences.items():
    folder = str(floor_100(length)*100) + '-' + str(floor_100(length)*100 + 99)
    path = folder + '\\' + 'sequence' + str(i) + '.txt'
    output = open(path, 'w')
    output.write(sequence)
    i += 1