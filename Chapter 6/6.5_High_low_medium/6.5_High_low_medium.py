# In the chapter_6 folder in the exercises download, you'll find a text file called 
# data.csv, containing some made-up data for a number of genes. Each line contains 
# the following fields for a single gene in this order: species name, sequence, gene 
# name, expression level. The fields are separated by commas (hence the name of the 
# file – csv stands for Comma Separated Values). Think of it as a representation of a 
# table in a spreadsheet – each line is a row, and each field in a line is a column. All 
# the exercises for this chapter use the data read from this file. 

# For each gene, print out a message giving the gene name and saying whether its AT 
# content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 
# and 0.65).

file = open("data.csv")

for line in file:
    # Turns every row into a list that contains the name of the species, the gene sequence, the gene name and expression level
    line_as_list = line.split(",")
    at_content = (line_as_list[1].count("a") + line_as_list[1].count("t"))/len(line_as_list[1])
    if at_content > 0.65:
        print(line_as_list[2] + " AT content is high")
    elif at_content < 0.45:
        print(line_as_list[2] + " AT content is low")
    else:
        #AT content between 0.45 and 0.65 (both included)
        print(line_as_list[2] + " AT content is medium")

file.close()