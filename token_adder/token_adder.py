"""
Simple script to format token list into switch statement for cs230 - Programming Languages lab 3
"""

# starting token const
token_const = 258

file1 = open("/Users/derrelldowney/projects/code/scripts/token_adder/tokens.txt", "r")
file2 = open("/Users/derrelldowney/projects/code/scripts/token_adder/get_token_name_switch.txt", "w")

line = file1.readline()
while line != '':
    
    token_name = line.rstrip('\n') 
    print(token_name)
    
    file2.write("case {}:\n\ttoken_name = \"{}\";\n\tbreak;\n".format(token_const, token_name))
    token_const = token_const+1
    line = file1.readline()






file1.close()
file2.close()