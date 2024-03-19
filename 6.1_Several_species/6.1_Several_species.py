# In the chapter_6 folder in the exercises download, you'll find a text file called 
# data.csv, containing some made-up data for a number of genes. Each line contains 
# the following fields for a single gene in this order: species name, sequence, gene 
# name, expression level. The fields are separated by commas (hence the name of the 
# file – csv stands for Comma Separated Values). Think of it as a representation of a 
# table in a spreadsheet – each line is a row, and each field in a line is a column. All 
# the exercises for this chapter use the data read from this file. 

# Print out the gene names for all genes belonging to Drosophila melanogaster or 
# Drosophila simulans. 

file = open("data.csv")

for line in file:
    # Turned every row into a list that contains the name of the species, the gene sequence, the gene name and expression level
    line_as_list = line.split(",")
    if line_as_list[0] == "Drosophila simulans" or line_as_list[0] == "Drosophila melanogaster":
        # The gene name is in the third column of each row
        print(line_as_list[2])