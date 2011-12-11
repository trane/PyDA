import argparse

parser = argparse.ArgumentParser(description='Run an NPDA on a string.')
parser.add_argument('string', metavar='"S"', type=str, nargs='+',
                           help='any number of strings')
parser.add_argument('-f', '--file', dest='file', help='loads an JSON encoded NPDA and runs the string(s) on it')
parser.add_argument('-p', '--print', dest='print', help='print an NPDA loaded from a file')
args = parser.parse_args()
parser.print_help()

def to_dot():
    print("")

# main method
#
# Verify arguements using argparse
#
# if the step flag isn't set, just test if the pda accepts the string and return the results
#
# if the step flag is set, go into a loop:
#
#   Get intput from user:
#   q = quit
#   f ID = freeze the stepper with that id
#   s = steps through everything that isn't frozen by 1 step
#   p = print the current data from the steppers, distingusihg between frozen and active
#
#   Act according to the input. Need to decide how to close (think don't close the
#   program until explicatally told to by the user pressing q)
