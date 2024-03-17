# Write a function that takes two arguments – a protein sequence and an amino acid 
# residue code – and returns the percentage of the protein that the amino acid makes
# up. Use the following assertions to test your function:

# assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
# assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
# assert my_function("MSRSLLLRFLLFLLLLPPLP", "L") == 50
# assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

def percent_aa(protein, aa):
    # the argument "aa" should not be case sensitive (see line 18)
    aa = aa.upper()
    number_aa = protein.count(aa)
    percent = (number_aa/len(protein))*100
    return percent

assert percent_aa("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert percent_aa("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert percent_aa("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert percent_aa("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
