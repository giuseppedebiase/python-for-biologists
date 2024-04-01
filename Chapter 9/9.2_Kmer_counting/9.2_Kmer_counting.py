'''
In the chapter_9 folder in the exercises download there is a collection of files with 
the extension .dna which contain DNA sequences of varying length, one per line. 
Use this set of files for both exercises. 
Write a program that will calculate the number of all kmers of a given length across
all DNA sequences in the input files and display just the ones that occur more than 
a given number of times. You program should take two command line arguments – 
the kmer length, and the cutoff number. 
'''

import sys
import os

print('Running...')
def generate_kmers(sequence, kmer_length):
    seq_len = len(sequence)
    start = 0
    end = start + kmer_length
    
    while end <= seq_len:
        kmers.append(sequence[start:end])
        start += 1
        end += 1

kmer_len = int(sys.argv[1])
freq = int(sys.argv[2])

#list that contains all the kmer of length kmer_len
kmers = []

for file in os.listdir('.'):
    if file.endswith('.dna'):
        file = open(file)
        for sequence in file:
            sequence = sequence.rstrip('\n')
            generate_kmers(sequence, kmer_len)

#dict that contains key:value kmer:freq of that kmer
kmer_freq = {}

for kmer in kmers:
    kmer_freq[kmer] = kmers.count(kmer)

for kmer, frequency in kmer_freq.items():
    if frequency > freq:
        print(kmer, frequency)

print('Done')