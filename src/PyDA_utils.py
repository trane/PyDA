"""
PyDA_utils.py

This file includes all of our utility methods, such as the JSON normalize
method, and functionality to print NPDA objects to .dot and .pdf files

Public API:
    normalize(pda) - Convert JSON object to our dictionary PDA representation
    pda2dot(npda_obj, pdaname) - Print npda_obj to 'pdaname.dot'
    pda2pdf(npda_obj, pdaname) - Print npda_obj to 'pdaname.pdf'
"""

import os
import json

## Main external API methods ##################################################

def load_dfa(filename):
    """
    Loads a dfa from a given json formatted file
    If the file loads and parses correctly, the pyda json structure is returned.
    If there was an error loading or parsing the file, None is returned.
    """
    try:
        json_data = open(filename)
        pyda_struct = json.load(json_data)
        json_data.close()
    except Exception:
        return None

    return pyda_struct

def normalize(pda):
    """ While JSON datastructure allows us portability, we will convert this
    into a more functional construct.
    PDAs will look like this:
    {
        'Q': {'s2', 's1', 's0'},
        'F': {'s2'},
        'Sigma': {'1', '0'},
        'Gamma': {'1', '0', 'Z'},
        'Delta': {
            ('s0', '1', '0', 's1', '0'),
            ('s2', '0', '0', 's1', '0'),
            ('s0', '0', '0', 's1', '0'),
            ('s0', '1', '1', 's2', '0'),
            ('s2', '0', '1', 's2', '0'),
            ('s1', '0', '0', 's1', '0'),
            ('s1', '1', '1', 's2', '0')
        },
        'q0': 's0',
        'Z': 'Z'
    }
    """
    npda = dict()
    npda['Q'] = set(pda['Q'])
    npda['Sigma'] = set(pda['Sigma'])
    npda['Gamma'] = set(pda['Gamma'])
    delta = set()
    for init,inputs in pda['Delta'].items():
        for inpt,stack in inputs.items():
            for stack_t,dest in stack.items():
                for state in dest[0]:
                    delta.add((init, inpt, stack_t, state, dest[1]))
    npda['Delta'] = delta
    npda['F'] = set(pda['F'])
    npda['q0'] = pda['q0']
    return npda

def pda2dot(npda_obj, pdaname):
    """Generate a .dot file for the given NPDA object and pda_name

    NOTE:  The .dot part of the filename should not be included in pdaname
    """
    with open(pdaname + '.dot', 'w') as fl:
        prDotHeader(fl)
        prNodeDefs(fl, npda_obj.pda)
        prOrientation(fl)
        prEdges(fl, npda_obj.pda)
        prClosing(fl)

def pda2pdf(npda_obj, pdaname):
    """Generate a .pdf file for the given NPDA object and pda_name

    NOTE:  The .pdf part of the filename should not be included in pdaname
    """
    with open(pdaname + '.dot', 'w') as fl:
        prDotHeader(fl)
        prNodeDefs(fl, npda_obj.pda)
        prOrientation(fl)
        prEdges(fl, npda_obj.pda)
        prClosing(fl)

    os.system("dot -Tps " + pdaname + ".dot > " + pdaname + ".ps")
    os.system("ps2pdf13 " + pdaname + ".ps")
    os.system("rm " + pdaname + ".dot " + pdaname + ".ps")


## Helper methods #############################################################

def dotsan_map(x):
    """A homomorphism. We need to sanitize set() also. Ugh!
    """
    if x in {  "{",   " ",   "'",   "}" }:
        return ""
    elif x == ",":
        return "_"
    elif x == "(":
        return "\("
    elif x == ")":
        return "\)"
    else:
        return x

def homos(S,f):
    """String homomorphism wrt lambda f
    """
    return "".join(map(f,S))

def dot_san_str(S):
    """Make dot like strings which are in set of states notation.
    """
    if S=="set()":
        return "EMPTY_SET"
    else:
        return homos(S, dotsan_map)

def prDotHeader(fl):
    print (r'digraph G {', file=fl)
    print (r'/* Defaults */', file=fl)
    print (r'  fontsize = 12;', file=fl)
    print (r'  ratio = compress; ', file=fl)
    print (r'  rankdir=LR; ', file=fl)
    print (r'/* Bounding box */', file=fl)
    print (r'   size = "4,4";', file=fl)

def prNonFinalNodeName(fl, q):
    print (dot_san_str(q), r'[shape=circle, peripheries=1];', file=fl)

def prFinalNodeName(fl, q):
    print(dot_san_str(q), file=fl, end='')  # No \n
    print(r' [shape=circle, peripheries=2];', file=fl)

def prOrientation(fl):
    print(r'/* Orientation */', file=fl)
    print(r'orientation = portrait;', file=fl)

def prEdges(fl, npda):
    print(r'/* The graph itself */', file=fl)
    print(r'""  -> ', dot_san_str(npda["q0"]), ";", file=fl)
    for QcQ in npda["Delta"]:
        print(dot_san_str(QcQ[0]), r' -> ', dot_san_str(QcQ[3]),
              r'[label="', dot_san_str(QcQ[1]) + ',',
              dot_san_str(QcQ[2]) + ';', dot_san_str(QcQ[4]), r'"];', file=fl)

def prClosing(fl):
    print(r'/* Unix command: dot -Tps exdfa.dot >! exdfa.ps */', file=fl)
    print(r"/* For further details, see the `dot' manual    */", file=fl)
    print(r"}", file=fl)

def prNodeDefs(fl, npda):
    print(r'/* Node definitions */', file=fl)
    print(r'  "" [shape=plaintext];', file=fl)  # Start state arrow is from "" to I
    # All non-accepts are single circles
    for q in npda["Q"] - npda["F"]:
        prNonFinalNodeName(fl, q)
    for q in npda["F"]:
        prFinalNodeName(fl, q)

