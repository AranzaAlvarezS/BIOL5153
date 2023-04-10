#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description = "This script will resturn the GFF and the FASTA files")

# addinng positional (required) arguments
parser.add_argument("gff", help = "The GFF file to parse ", type = str)
parser.add_argument("fasta", help = "The FASTA file to parse", type = str)

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args() 

# open gff file
with open(args.gff) as x: #with this open, do these things
    # loop over all lines in a file
    for line in x:
        print(line)









