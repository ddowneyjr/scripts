"""
Simple script to format token list into switch statement for cs230 - Programming Languages lab 3

Works well besides after each line read theres a \n which means that you need to manually delete each new line
Not a big enough deal that I need to fix it right now but something to improve later if needed
"""

# starting token const
token_const = 258

file1 = open("/Users/derrelldowney/projects/code/scripts/token_adder/tokens.txt", "r")
file2 = open("/Users/derrelldowney/projects/code/scripts/token_adder/get_token_name_switch.txt", "w")

line = file1.readline()
while line != '':
    token_name = line 
    for token in token_name:
        file2.write("case {}:\n\ttoken_name = \"{}\";\n\tbreak;\n".format(token_const, token))
        token_const = token_const+1
    line = file1.readline()






file1.close()
file2.close()