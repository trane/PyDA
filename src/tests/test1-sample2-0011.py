#!/usr/bin/env python3

# Test sample2 with the string "0011"
# npda.py and PyDA_utils.py should be symlinked into same directory

from npda import *
from PyDA_utils import *

the_pda = normalize(load_pda('samples/sample2-0n1n.pyda'))
n = NPDA(the_pda, "0011")

for i in range(10):
    n.step_all()
    if n.accepts():
        print("WOOHOO!")
        break
