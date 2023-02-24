"""
Simple script to format token list into switch statement for cs230 - Programming Languages lab 3
"""

# starting token const
token_const = 258

# path for file 1
file1_path = "/Users/derrelldowney/projects/code/scripts/token_adder/tokens.txt"
# path fr file 2
file2_path = "/Users/derrelldowney/projects/code/scripts/token_adder/get_token_name_switch.txt"

file1 = open(file1_path, "r")
file2 = open(file2_path, "w")

line = file1.readline()

# staying in the while loop until the EOF
while line != '':
    
    token_name = line.rstrip('\n') 
    # print(token_name)
    
    # writing the switch format to file2
    file2.write("case {}:\n\ttoken_name = \"{}\";\n\tbreak;\n".format(token_const, token_name))
    token_const = token_const+1
    line = file1.readline()






file1.close()
file2.close()