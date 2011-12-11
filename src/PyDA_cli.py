import argparse
from npda import *
from PyDA_utils import *

parser = argparse.ArgumentParser(description='Run an NPDA on a string.')
parser.add_argument('string', metavar='"S"', type=str, nargs='+',
                           help='any number of strings')
parser.add_argument('-f', '--file', dest='file', help='loads an JSON encoded NPDA and runs the string(s) on it')
parser.add_argument('-p', '--print', dest='print', help='print an NPDA loaded from a file')
args = parser.parse_args()
parser.print_help()

def to_dot():
    print("")

def main():
    # Verify arguements using argparse
    # pdf_file
    # step
    # test_string

    # Create the npda
    pda = normalize(load_pda(pda_file))
    n = NPDA(the_pda, test_string)

    # Default behaivor, check if the string satisfies the pda
    if(step == False):
        if check_acceptance(n) == True:
            print("The string \"" + test_string + "\" satisfies this pda.")
        else:
            print("The string \"" + test_string + "\" does not satisfies this pda.")
        return

    # Main event loop for stepping through the program
    while True:
        # Get intput from user: 
        # TODO - break this up to multiple works (for things like pdf FILENAME)
        # or maybe just use argparse here as well if possible.
        cmd = input("Enter a command: ")

        # Process the user input
        if cmd == "q":
            return
        else if cmd == "s":
            return
        else if cmd == "p":
            return
        else if cmd == "f":
            return
        else if cmd == "t":
            return
        else if cmd == "pdf":
            return
        else if cmd == "dot":
            return
        else:
            print("q: Quit the program")
            print("s: Steps ever thread that isn't frozen by one position")
            print("p: Print the current state of all the threads")
            print("f ID: Freeze the thead with ID from stepping")
            print("t ID: Thaw the thread ID to continue stepping")
            print("pdf FILENAME: Creates a pdf file of this NPDA with the given filename")
            print("dot FILENAME: Creates a dot file of this NPDA with the given filename")
