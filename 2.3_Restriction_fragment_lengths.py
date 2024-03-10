# Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
# The sequence contains a recognition site for the EcoRI restriction enzyme, which
# cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk). 
# Write a program which will calculate the size of the two fragments that will be
# produced when the DNA sequence is digested with EcoRI.

my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" 
#                              ^      
p = my_dna.find("GAATTC") #p is 21
# When using string[numer1:nuber2] the positions are inclusve at the start but exclusive at the end
# fragment1 slices the string from the beginning to the position+1 (EcoRI cuts after the G in GAATTC)
fragment1 = my_dna[0:p+1]
# look line 11. p+1 is not included so the second fragment will start with AATTC...
fragment2 = my_dna[p+1:len(my_dna)]
print("The length of the DNA fragments after the EcoRI digestion will be " + str(len(fragment1)) + " and " + str(len(fragment2)) + "nt long")
