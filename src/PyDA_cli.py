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
        #   Get intput from user:
        #   q = quit
        #   f ID = freeze the stepper with that id
        #   s = steps through everything that isn't frozen by 1 step
        #   p = print the current data from the steppers, distingusihg between frozen and active
        #   pdf FILENAME = create a pdf document of the current pda
        #   dot FILENAME = create a dotty document of the current pda
        #
        #   Act according to the input. Need to decide how to close (think don't close the
        #   program until explicatally told to by the user pressing q)
