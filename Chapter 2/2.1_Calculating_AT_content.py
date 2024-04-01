'''
Here's a short DNA sequence:
ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
Write a program that will print out the AT content of this DNA sequence. Hint: you
can use normal mathematical symbols like add (+), subtract (-), multiply (*), divide 
(/) and parentheses to carry out calculations on numbers in Python. 
'''
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
AT_count = my_dna.count("A") + my_dna.count("T")
#The formula for calculating AT content is n° of A+T/length of the sequence
print("AT content of my_dna sequence is: " + str(AT_count/len(my_dna)))
