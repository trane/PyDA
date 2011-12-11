from npda import *
from PyDA_utils import *

esc = "\x1b["

codes = {}
codes["reset"]     = esc + "39;49;00m"

dark_colors  = ["black", "darkred", "darkgreen", "brown", "darkblue",
                "purple", "teal", "lightgray"]
light_colors = ["darkgray", "red", "green", "yellow", "blue",
                "fuchsia", "turquoise", "white"]

x = 30
for d, l in zip(dark_colors, light_colors):
    codes[d] = esc + "%im" % x
    codes[l] = esc + "%i;01m" % x
    x += 1

del d, l, x

def print_accept(s):
    print(color_state(s, 'green'))

def print_frozen(s):
    print(color_state(s, 'blue'))

def print_reject(s):
    print(color_state(s, 'red'))

def print_state(s):
    print(format_state(s))

def format_state(s):
    return str(s.ident) + "\t" + s.state + "\t" + s.inpt + "\n" + s.stack

def color_state(s, color):
    result = ""+codes[color]
    result += format_state(s)
    result += codes['reset']
    result += "\n\n"
    return result


def print_step_help():
    print("q: Quit the program")
    print("s: Steps ever thread that isn't frozen by one position")
    print("p: Print the current state of all the threads")
    print("f ID: Freeze the thead with ID from stepping")
    print("t ID: Thaw the thread ID to continue stepping")
    print("pdf FILENAME: Creates a pdf file of this NPDA with the given FILENAME")
    print("dot FILENAME: Creates a dot file of this NPDA with the given FILENAME")

def print_states(npda):
    for s in npda.stepper_list:
        if len(s.stack) <= 1 and len(s.inpt) == 0:
            print_accept(s)
        else:
            print_state(s)

    for s in npda.frozen_list:
        print_frozen(s)

    for s in npda.reject_list:
        print_reject(s)

def freeze_helper(npda, sid):
    if sid == None:
        print_step_help()
        return

    try:
        ident = int(sid)
    except:
        print(sid + ": is not a valid ID")
        return

    if npda.freeze(ident) == True:
        print(sid + ": Frozen")
    else:
        print(sid + ": is not currently stepping")

def thaw_helper(npda, sid):
    if sid == None:
        print_step_help()
        return

    try:
        ident = int(sid)
    except:
        print(sid + ": is not a valid ID")
        return

    if npda.thaw(ident) == True:
        print(sid + ": Thawed")
    else:
        print(sid + ": is not currently frozen")

def pdf_helper(npda, filename):
    if filename == None:
        print_step_help()
    else:
        pda2pdf(npda, filename)

def dot_helper(npda, filename):
    if filename == None:
        print_step_help()
    else:
        pda2dot(npda, filename)

def load(filename):
    return normalize(load_pda(filename))

def main(filename, string):
    # Verify arguements using argparse
    # pdf_file
    # step
    # test_string
    # Create the npda
    print("Loading " + filename)
    print("Running on string: " + string)
    step = True
    pda = load(filename)
    n = NPDA(pda, string)

    # Default behaivor, check if the string satisfies the pda
    if(step == False):
        if check_acceptance(n) == True:
            print("The string \"" + string + "\" satisfies this pda.")
        else:
            print("The string \"" + string + "\" does not satisfies this pda.")
        return

    # Main event loop for stepping through the program
    while True:
        # Get and parse input from the user
        usr_inpt = input("\nEnter a command (h for help): ")
        argv = usr_inpt.split()
        argc = len(argv)
        if argc == 0:
            print_step_help()
            continue
        elif argc == 1:
            cmd = argv[0]
            arg = None
        else:
            cmd = argv[0]
            arg = argv[1]

        # Process this command
        if cmd == "q": # Quit
            print("Exiting the program")
            return
        elif cmd == "s": # Step
            n.step_all()
            print_states(n)
        elif cmd == "p": # Print
            print_states(n)
        elif cmd == "f": # Freeze a stepper
            freeze_helper(n, arg)
        elif cmd == "t": # Thaw a stepper
            thaw_helper(n, arg)
        elif cmd == "pdf":
            pdf_helper(n, arg)
        elif cmd == "dot":
            dot_helper(n, arg)
        else:
            print_step_help()

