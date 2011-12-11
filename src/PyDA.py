#!/usr/bin/env python3
import argparse
import PyDA_cli

parser = argparse.ArgumentParser(description='Run an NPDA on a string.')
parser.add_argument('test_string', nargs='?',
                           help='input string for the NPDA (defaults 000111)',
                           default='000111' )
parser.add_argument('-s', '--step', help='Steps through a NPDA to \
        to view state and freeze/thaw specific threads',
        action='store_true', required=False)
parser.add_argument('-f', '--file', help='loads an JSON encoded \
        NPDA and runs the string(s) on it (defaults to sample2-0n1n.pyda)',
        default='samples/sample2-0n1n.pyda', required=False)
args = parser.parse_args()

PyDA_cli.main(args.file, args.test_string, args.step)
