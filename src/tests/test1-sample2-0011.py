#!/usr/bin/env python3

# Test sample2 with the string "0011"
# npda.py and PyDA_utils.py should be symlinked into same directory

from npda import *
from PyDA_utils import *

# The string we will be testing
test_string = "0011"

# Load the pda from the json file into our program
the_pda = normalize(load_pda('../samples/sample2-0n1n.pyda'))
n = NPDA(the_pda, test_string)

# Step this string through the pda
while n.can_step:
    n.step_all()
    if n.accepts():
        break

if n.accepts():
    print("The string " + test_string + " satisfies this pda.")
else:
    print("The string " + test_string + " does not satisfies this pda.")

