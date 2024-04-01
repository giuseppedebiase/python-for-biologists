'''
Here's a short DNA sequence:
ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
Write a program that will print the complement of this sequence.
'''
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
my_dna_lower = my_dna.lower()
#replace is case sensitive, so I used the lower method to convert uppercase letters to lower case and then I used replace to replace lower case bases to their complementary (in uppercase)
my_dna_a_T = my_dna_lower.replace("a", "T")
my_dna_t_A = my_dna_a_T.replace("t", "A")
my_dna_c_G = my_dna_t_A.replace("c", "G")
my_dna_g_C = my_dna_c_G.replace("g", "C")
print("The complemntary sequence of my_dna is: " + my_dna_g_C)
