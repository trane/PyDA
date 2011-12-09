import os

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

def pda2dot(npda_obj, fname):
    """Generate a .dot file with the given filename for the given NPDA object
    """
    with open(fname, 'w') as fl:
        prDotHeader(fl)
        prNodeDefs(fl, npda_obj.pda)
        prOrientation(fl)
        prEdges(fl, npda_obj.pda)
        prClosing(fl)

def pda2pdf(npda_obj, pdaname):
    """Generate a .pdf file for the given NPDA object and pda_name
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

