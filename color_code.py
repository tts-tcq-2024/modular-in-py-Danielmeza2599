# Daniel Meza
# Jr Embedded Software Developer
# color_code.py



# Color_code.py: It will contain the functions related to the conversion between even numbers and colors.

MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def get_color_from_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    if major_index >= len(MAJOR_COLORS):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    if minor_index >= len(MINOR_COLORS):
        raise Exception('Minor index out of range')
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    try:
        major_index = MAJOR_COLORS.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = MINOR_COLORS.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(MINOR_COLORS) + minor_index + 1



# Function generate_color_code_reference: 
# This function generates a list of strings representing the correspondence between pair numbers and colors.
def generate_color_code_reference():
    reference = []
    for pair_number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        reference.append(f"{pair_number}: {color_pair_to_string(major_color, minor_color)}")
    return reference
