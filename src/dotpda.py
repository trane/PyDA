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

def prEdges(fl, D):
    print(r'/* The graph itself */', file=fl)
    print(r'""  -> ', dot_san_str(D["q0"]), ";", file=fl)
    for QcQ in D["Delta"].items():
        print(dot_san_str(QcQ[0][0]), r' -> ', dot_san_str(QcQ[1]), r'[label="', dot_san_str(QcQ[0][1]), r'"];', file=fl)

def prClosing(fl):
    print(r'/* Unix command: dot -Tps exdfa.dot >! exdfa.ps */', file=fl)
    print(r"/* For further details, see the `dot' manual    */", file=fl)
    print(r"}", file=fl)

def prNodeDefs(fl, D):
    print(r'/* Node definitions */', file=fl)
    print(r'  "" [shape=plaintext];', file=fl)  # Start state arrow is from "" to I
    # All non-accepts are single circles
    for q in D["Q"] - D["F"]:
        prNonFinalNodeName(fl, q)
    for q in D["F"]:
        prFinalNodeName(fl, q)

def dot_pda(D, fname):
    """Generate a dot file with the automaton in it. Run the dot file through
    dot and generate a ps file.
    """
    fl = open(fname, 'w')
    #-- digraph decl
    prDotHeader(fl)
    #-- node names and how to draw them
    prNodeDefs_w_bh(fl, D)
    #-- orientation - now landscape
    prOrientation(fl)
    #-- edges
    prEdges_w_bh(fl, D)
    #-- closing
    prClosing(fl)

def prNFAEdges(fl, N):
    """Suppress BH.
    """
    print(r'/* The graph itself */', file=fl)
    print(r'""  -> ', dot_san_str(N["q0"]), ";", file=fl)
    for QcQ in N["Delta"].items():
        for nxt_state in QcQ[1]:
            print(dot_san_str(QcQ[0][0]), r' -> ', dot_san_str(nxt_state), r'[label="', dot_san_str(ShowEps(QcQ[0][1])), r'"];', file=fl)

