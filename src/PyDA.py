# PyDA

# A way to provide a pda as a string to this program

# A structure to hold the pda
    # A stack for the pda
    # Nodes, which contain pointers to other nodes based on input

# A way to parse strings and move them into the pda
    # Have a function that takes a string being checked against the pda and moves
    # it forwards by one step

# A way to step through the pda, one thing at a time, and display that input somehow
    # SDL?

# A way to non-deterministacally create more pdas as we step through them
    # Copy everything to a new pda data structure, then have the step method
    # step through both of the resulting pda's
