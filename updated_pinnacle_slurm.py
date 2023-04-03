#! /usr/bin/env python3

# import modules
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser(description = "This script creates a SLURM file for jobs on the AHPCC cluster")

# add positional (required) arguments
parser.add_argument("job_name", help = "Name of the job", type = str)

# add optional arguments 
#'--',shows arg parse that this is optional, both are recognized and equivalent
parser.add_argument('-q','--queue', help = 'Requested queue (comp1, comp6, comp72), (default = comp72)', default = 'comp72', type = str) #shows arg parse that this is optional, both are recognized and equivalent

parser.add_argument('-n','--nodes', help = 'Number of nodes to request (default =1)', default = '1', type = int) #shows arg parse that this is optional, both are recognized and equivalent


parser.add_argument('-p','--processors', help = 'Number of processors to request (default = 24)', default = '24', type = int) #shows arg parse that this is optional, both are recognized and equivalent


parser.add_argument('-w','--walltime', help = 'Length of the job (default = 72)', default = '72', type = int) #shows arg parse that this is optional, both are recognized and equivalent

# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args() 


print('#!/bin/bash')
print()
print('#SBATCH --job-name=' + args.job_name) #job name
print('#SBATCH --partition',args.queue) #queue
print('#SBATCH --nodes=' + str(args.nodes)) #number of nodes
print('#SBATCH --tasks-per-node=',args.processors) #number of processors
print('#SBATCH --time='+ str(args.walltime) + ':00:00')#walltime
print('#SBATCH -o %j.out')
print('#SBATCH -e %j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=aranzaa@uark.edu')
print()
print('module purge') #purge modules
print()
print('cd $SLURM_SUBMIT_DIR')
print()
print('#job command here')
