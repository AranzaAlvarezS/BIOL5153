#! /usr/bin/env python3

# import modules
import argparse
import csv
from Bio import SeqIO
# create an ArgumentParser object
parser = argparse.ArgumentParser(description = "This script will resturn the GFF and the FASTA files")

# addinng positional (required) arguments
parser.add_argument("gff", help = "The GFF file to parse ", type = str)
parser.add_argument("fasta", help = "The FASTA file to parse", type = str)


# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args() 

# read in the FASTA file 
genome = SeqIO.read(args.fasta, "fasta") # seqIO organizes fasta into name, descriptuion, sequence, etc
#print(genome.seq[start,end]) # printing the seq object 


# open gff file
with open(args.gff) as gff_file: #with this open, do these things (with automatically closes)
    # create a csv reader object
    reader = csv.reader(gff_file, delimiter = '\t')
    # loop over all lines in a file
    for line in reader:

        #skip blank lines
        if not line:
            continue # don't do anything and go to the next line

        #else it's not a blank line
        else: 
            #line = line.strip()
            #print(line)
            #split line on tab characters
            #columns = line.split('\t') # Strip line breaks from the current line
            #line = line.strip('\t')

            #give variable names to the columns
            organism = line[0]
            source = line[1]
            feature_type = line[2]
            start = int(line[3])
            end = int(line[4])

            # add the length to column 5
            line[5] = str(end - start + 1) # we add the one as the end is not inclusive

            length = line[5]
            strand = line[6]
            attributes = line[8]

           # extract the feature
            feature_seq = genome.seq[start -1:end]
           

            # print FASTA output for this feature

            print(">" + organism, feature_type, attributes)
            print(feature_seq)
            #print(len(feature_seq) - ((end-start)+1))
            
            # add the length to column 5
            # line[5] = str(end - start + 1) # we add the one as the end is not inclusive

            # join takes as an argument a list and it joins the element on a list at one charcter
                # x = "charcter that we want to join at".join(list)
            #new_line = '\t'.join(line)
            # print(new_line)
