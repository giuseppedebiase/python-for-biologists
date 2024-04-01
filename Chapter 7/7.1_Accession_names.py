'''
Here's a list of made-up gene accession names:
xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp
Write a program that will print only the accession names that satisfy the following 
criteria – treat each criterion separately:
• contain the number 5
• contain the letter d or e
• contain the letters d and e in that order
• contain the letters d and e in that order with a single letter between them
• contain both the letters d and e in any order
• start with x or y
• start with x or y and end with e
• contain three or more numbers in a row
• end with d followed by either a, r or p
'''

import re

accession_names = "xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp"
accession_names = accession_names.replace(" ", "")
accession_list = accession_names.split(",")

contain_five = []
contain_d_or_e = []
contain_de = []
contain_d_anything_e = []
contain_d_e_any_order = []
start_x_or_y = []
start_x_or_y_end_e = []
contain_minimum_three_numbers_in_a_row = []
end_da_dr_dp = []

#this exercise is in the chapter that covers regular expression, so I just used regex
for accession in accession_list:
    #contain the number 5
    if re.search(r"5", accession):
        contain_five.append(accession)

    #contain d or e
    if re.search(r"(d|e)", accession):
        contain_d_or_e.append(accession)
    
    #contain d and e in that order
    if re.search(r"d.*e", accession):
        contain_de.append(accession)

    #contain d and e in that order with a single letter between them
    if re.search(r"d.e", accession):
        contain_d_anything_e.append(accession)

    #contain both the letters d and e in any order
    #in theory this should add to the list only the accession names that contain the following pattern: d[any n.° of letters]e or e[any n.° of letters]d
    #in the script given by the author as a solution the if statement for this part is the following:
    #if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
    #which matches "d[any n.° of letters]e or e[any n.° of letters]d" concept
    #and gives as output the following ac names when run: eihd39d9, chdsye847, hdle3455, xjhd53e, de37dp
    #hwoever in the book it's written that the acc names that should be given as the output should be: hedle3455, de37dp
    #so the acc names shouldn't contain the patterns "d[any n.° of letters]e" or "e[any n.° of letters]d" but just "de" or "ed"
    if re.search(r"de|ed", accession):
        contain_d_e_any_order.append(accession)
    
    #start with x or y
    if re.search(r"^(x|y)", accession):
        start_x_or_y.append(accession)

    #start with x or y and end with e
    if re.search(r"^(x|y).*e$", accession):
        start_x_or_y_end_e.append(accession)

    #contain three of more numbers in a row
    #this if works because acc names with 4 (or more) numbers are basically acc names 
    #that contain 3 numbers followed by 1 (or more) numbers
    if re.search(r"[0123456789]{3}", accession):
        contain_minimum_three_numbers_in_a_row.append(accession)
    
    #end with d followed by either a, r or p
    if re.search(r"d[arp]$", accession):
        end_da_dr_dp.append(accession)

print("accession names that contain 5:")
print(contain_five)
print("accession names that contain the letter d or e:")
print(contain_d_or_e)
print("accession names that contain the letters d and e in that order:")
print(contain_de)
print("accession names that contain the letters d and e in that order with a single letter between them:")
print(contain_d_anything_e)
print("accession names that contain both the letters d and e in any order:")
print(contain_d_e_any_order)
print("accession names that start with x or y:")
print(start_x_or_y)
print("accession names that start with x or y and end with e:")
print(start_x_or_y_end_e)
print("accession names that contain minimum 3 or more numbers in a row:")
print(contain_minimum_three_numbers_in_a_row)
print("accession names that end with d followed by either a, r or p:")
print(end_da_dr_dp)
