# PyDA

# List containing all of the PDA's that we will step through in the step method
stepping = list();

# A way to provide a pda as a string to this program

# A structure to hold the pda
    # A stack for the pda
    # Nodes, which contain pointers to other nodes based on input

# A way to parse strings and move them into the pda
    # Have a function that takes a string being checked against the pda and moves
    # it forwards by one step

# Steps through all of the PDA's in the stepping list by one move, creating new
# PDA's if non-determinism kicks in, and adds those to the stepping list as well
def step():
    return

# A way to non-deterministacally create more pdas as we step through them
    # Copy everything to a new pda data structure, then have the step method
    # step through both of the resulting pda's
