"""
Name: Jackson McAfee
Date: August 28, 2023
Assignment: Assignment 1
Due Date: Septmber 3, 2023
About this project: Basic Caesar cipher encoder in Python. 
All work below was performed by Jackson McAfee
"""

# 
from string import ascii_uppercase

def main():
    # get int shift value
    shift = -1
    while (shift < 0):
        shift = int(input("Enter in the positive number greater than zero for the number of characters to be shifted: "))
        shift = shift % 26

    print (shift)

    # get direction to shift in
    direction = ""
    while (direction != "R" and direction != "L"):
        direction = input("Enter in R (for Right) or L (for Left) for the direction of the shift: ").upper()

    # get text to shift
    text = ""
    while (text == ""):
        text = input("Enter in the text: ").upper()

    # shift and append each character
    shifted_string = ""
    for ch in text:
        # if non-alphabetical character, ignore and append
        if not ch.isalpha():
            shifted_string += ch
        # otherwise, shift based on the passed character
        else:
            if (direction == "R"):
                val = ord(ch) - 65 + shift
            else:
                val = ord(ch) - 65 - shift

            # modulo 26 to prevent access errors
            val = val % 26
            shifted_string += ascii_uppercase[ val ]

    print("Converted string: ", shifted_string)

main()