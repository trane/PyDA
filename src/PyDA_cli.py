import argparse
from npda import *
from PyDA_utils import *

#parser = argparse.ArgumentParser(description='Run an NPDA on a string.')
#parser.add_argument('string', metavar='"S"', type=str, nargs='+',
#                           help='any number of strings')
#parser.add_argument('-f', '--file', dest='file', help='loads an JSON encoded NPDA and runs the string(s) on it')
#parser.add_argument('-p', '--print', dest='print', help='print an NPDA loaded from a file')
#args = parser.parse_args()
#parser.print_help()

def to_dot():
    print("")

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
        print("" + str(s.ident) + "\t" + s.state + "\t" + s.inpt + "\n" + s.stack + "\n\n")

    for s in npda.frozen_list:
        print("" + str(s.ident) + "\t" + s.state + "\t" + s.inpt + "\n" + s.stack + "\n\n")

def main():
    # Verify arguements using argparse
    # pdf_file
    # step
    # test_string

    # Create the npda
    step = True 
    test_string = '000111'
    pda = normalize(load_pda('samples/sample2-0n1n.pyda'))
    n = NPDA(pda, test_string)

    # Default behaivor, check if the string satisfies the pda
    if(step == False):
        if check_acceptance(n) == True:
            print("The string \"" + test_string + "\" satisfies this pda.")
        else:
            print("The string \"" + test_string + "\" does not satisfies this pda.")
        return

    # Main event loop for stepping through the program
    while True:
        # Get and parse input from the user
        usr_inpt = input("\nEnter a command: ")
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

main()
