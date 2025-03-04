# Daniel Meza
# Jr Embedded Software Developer
# Main.py

#main.py: It will contain the main function to generate the reference manual.

import color_code



# Function print_color_code_reference: This function prints the reference manual on the console.
def print_color_code_reference():
    reference = color_code.generate_color_code_reference()
    for line in reference:
        print(line)

if __name__ == '__main__':
    print_color_code_reference()




 # Code splitting: The code has been split into three files to improve modularity and clarity.
