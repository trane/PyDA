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

def print_state(npda):
    print('todo')

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

        # TODO - break this up into lots of helper functions
        # Process the command text 
        if cmd == "q":
            print("Exiting the program")
            return
        elif cmd == "s":
            n.step_all()
            print_state(n)
        elif cmd == "p":
            print_state(n)                 # TODO - IMPLEMENT ME
        elif cmd == "f":
            if arg == None:
                print_step_help()
            elif n.freeze(arg) == True:
                print(arg + ": Frozen")
            else:
                print(arg + ": is not a valid ID")
        elif cmd == "t":
            if arg == None:
                print_step_help()
            elif n.thaw(arg) == True:
                print(arg + ": Thawed")
            else:
                print(arg + ": is not a valid ID")
        elif cmd == "pdf":
            if arg == None:
                print_step_help()
                continue
            pda2pdf(n, arg)
        elif cmd == "dot":
            if arg == None:
                print_step_help()
                continue
            pda2dot(n, arg)
        else:
            print_step_help()

main()
