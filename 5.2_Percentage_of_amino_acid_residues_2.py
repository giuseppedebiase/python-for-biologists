# Modify the function from part one so that it accepts a list of amino acid residues 
# rather than a single one. If no list is given, the function should return the 
# percentage of hydrophobic amino acid residues (A, I, L, M, F, W, Y and V). Your 
# function should pass the following assertions:

# assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
# assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
# assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
# assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65

def percent_aa(protein, aa_list = ["A", "I", "L", "M", "F", "W", "Y", "W"]):
    #number_aa is the number of all the aminoacids of the list list (the second argument of this function) present in the protein sequence 
    number_aa = 0
    for aminoacid in aa_list:
        number_aa = number_aa + protein.count(aminoacid)
    percentage = (number_aa/len(protein)) * 100
    return round(percentage, 1)

assert percent_aa("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert percent_aa("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert percent_aa("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert percent_aa("MSRSLLLRFLLFLLLLPPLP") == 65
