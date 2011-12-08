from lang import *
from dfa import *

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

def prNFAEmptySetNode(fl):
    print (dot_san_str("EMPTY"), r'[shape=circle, peripheries=1];', file=fl)    

def prFinalNodeName(fl, q):
    # Could write like print (q, r'[shape=circle, peripheries=2];', file=fl)
    # But am documenting use of trailing comma to suppress \n . In Python3 we supply end = ''
    print(dot_san_str(q), file=fl, end='') # end with no CR
    print(r' [shape=circle, peripheries=2];', file=fl) # end with a CR

def prOrientation(fl):
    print(r'/* Orientation */', file=fl)
    print(r'orientation = portrait;', file=fl)

def prEdges_w_bh(fl, D):
    print(r'/* The graph itself */', file=fl)
    print(r'""  -> ', dot_san_str(D["q0"]), ";", file=fl)
    for QcQ in D["Delta"].items():
        print(dot_san_str(QcQ[0][0]), r' -> ', dot_san_str(QcQ[1]), r'[label="', dot_san_str(QcQ[0][1]), r'"];', file=fl)

def prEdges(fl, D):
    """Suppress BH.
    """
    print(r'/* The graph itself */', file=fl)
    print(r'""  -> ', dot_san_str(D["q0"]), ";", file=fl)
    for QcQ in D["Delta"].items():
        if (((QcQ[0][0]) != "BH") & (QcQ[1] != "BH")):
            print(dot_san_str(QcQ[0][0]), r' -> ', dot_san_str(QcQ[1]), r'[label="', dot_san_str(QcQ[0][1]), r'"];', file=fl)        

def prClosing(fl):
    print(r'/* Unix command: dot -Tps exdfa.dot >! exdfa.ps */', file=fl)
    print(r"/* For further details, see the `dot' manual    */", file=fl)
    print(r"}", file=fl)        

def prNodeDefs_w_bh(fl, D):    
    print(r'/* Node definitions */', file=fl)
    print(r'  "" [shape=plaintext];', file=fl)  # Start state arrow is from "" to I
    # All non-accepts are single circles
    for q in D["Q"] - D["F"]:
        prNonFinalNodeName(fl, q)
    for q in D["F"]:        
        prFinalNodeName(fl, q)

def prNodeDefs(fl, D):
    """Suppress BH.
    """
    print(r'/* Node definitions */', file=fl)
    print(r'  "" [shape=plaintext];', file=fl)  # Start state arrow is from "" to I
    # All non-accepts are single circles
    for q in D["Q"] - D["F"]:
        if (q != "BH"):
            prNonFinalNodeName(fl, q)
    for q in D["F"]:        
        prFinalNodeName(fl, q)


def dot_dfa_w_bh(D, fname):
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

def dot_dfa(D1, fname):
    """Generate a dot file with the automaton in it. Run the dot file through
    dot and generate a ps file.
    """
    D = shrink_dfastates(D1)
    fl = open(fname, 'w')
    #-- digraph decl
    prDotHeader(fl)
    #-- node names and how to draw them
    prNodeDefs(fl, D)
    #-- orientation - now landscape
    prOrientation(fl)
    #-- edges
    prEdges(fl, D)
    #-- closing
    prClosing(fl)


def ShowEps(s):
    if (s==""):
        return "@"
    else:
        return s

def prNFAEdges(fl, N):
    """Suppress BH.
    """
    print(r'/* The graph itself */', file=fl)
    print(r'""  -> ', dot_san_str(N["q0"]), ";", file=fl)
    for QcQ in N["Delta"].items():
        for nxt_state in QcQ[1]:
            print(dot_san_str(QcQ[0][0]), r' -> ', dot_san_str(nxt_state), r'[label="', dot_san_str(ShowEps(QcQ[0][1])), r'"];', file=fl)        

def prClosing(fl):
    print(r'/* Unix command: dot -Tps exdfa.dot >! exdfa.ps */', file=fl)
    print(r"/* For further details, see the `dot' manual    */", file=fl)
    print(r"}", file=fl)        
    


def dot_nfa(N1, fname):
    """Generate a dot file with the automaton in it. Run the dot file through
    dot and generate a ps file.
    """
    print(N1)
    N = shrink_nfastates(N1)
    print(N)
    fl = open(fname, 'w')
    #-- digraph decl
    prDotHeader(fl)
    #-- node names and how to draw them
    prNodeDefs(fl, N)
    #-- orientation - now landscape
    prOrientation(fl)
    #-- edges
    prNFAEdges(fl, N)
    #-- closing
    prClosing(fl)
    

def shrink_nfastates(N):
    maxStNam = max(map(len, N["Q"]))
    if maxStNam <= 20:
        return N
    StateL = list(N["Q"])
    stateDict = { State_i : ("St" + str(i)) for i in range(0, len(StateL)) for State_i in StateL if State_i == StateL[i] }
    NewQ = { stateDict[q] for q in N["Q"] }
    NewDelta = { (stateDict[a], b) : {stateDict[c] for c in C} for ((a,b),C) in N["Delta"].items() } 
    Newq0 = stateDict[N["q0"]]
    NewF = { stateDict[f] for f in N["F"] }
    return mk_nfa(NewQ, N["Sigma"], NewDelta, Newq0, NewF)

def shrink_dfastates(D):
    maxStNam = max(map(len, D["Q"]))
    if maxStNam <= 20:
        return D
    StateL = list(D["Q"])
    stateDict = { State_i : ("St" + str(i)) for i in range(0, len(StateL)) for State_i in StateL if State_i == StateL[i] }
    NewQ = { stateDict[q] for q in D["Q"] }
    NewDelta = { (stateDict[a], b) : stateDict[c] for ((a,b),c) in D["Delta"].items() } 
    Newq0 = stateDict[D["q0"]]
    NewF = { stateDict[f] for f in D["F"] }
    return mk_dfa(NewQ, D["Sigma"], NewDelta, Newq0, NewF)


    
        
    


