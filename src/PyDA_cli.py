import argparse

parser = argparse.ArgumentParser(description='Run an NPDA on a string.')
parser.add_argument('string', metavar='"S"', type=str, nargs='+',
                           help='any number of strings')
parser.add_argument('-f', '--file', dest='file', help='loads an JSON encoded NPDA and runs the string(s) on it')
parser.add_argument('-p', '--print', nargs=0, dest='print', help='print an NPDA loaded from a file')
args = parser.parse_args()
parser.print_help()

def to_dot():
    print("")
