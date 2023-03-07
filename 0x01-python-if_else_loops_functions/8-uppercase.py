#!/usr/bin/pytho3
def uppercase(s):
    # Initialize an empty string to hold the uppercase version of the string
    upper_s = ""
    
    # Loop through each character in the string
    for c in s:
        # Convert the character to its uppercase equivalent using its ASCII code
        if ord(c) >= 97 and ord(c) <= 122:
            upper_c = chr(ord(c) - 32)
        else:
            upper_c = c
        
        # Append the uppercase character to the new string
        upper_s += upper_c
    
    # Print the uppercase string followed by a newline character
    print("{}\n".format(upper_s))

