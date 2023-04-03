#! /usr/bin/env python3

#assignment_5

# import modules
import argparse

#Defining Variables
job_name = 'assignment_5'
queue = 'comp 72'
nodes = '1'
number_of_processors = '32'
walltime = '02'
command = 'command1'

# create an ArgumentParser object
parser = argparse.ArgumentParser(description = "This script returns the job name of the slurm script")

# addinng positional (required) arguments
parser.add_argument("job", help = "The job name that you want to submit", type = str)

# add optional arguments: : queue, number of nodes, number of processors, walltime
# the default for 'store_true' is ... "False"
# if 'store_true', then assign 'True' with -v or --verbose.
parser.add_argument('-q','--queue', help = 'Print queue of job (default = simple output)', action = 'store_true') #shows arg parse that this is optional, both are recognized and equivalent
action = 'store_true'

parser.add_argument('-n','--nodes', help = 'Print number of nodes (default = simple output)', action = 'store_true') #shows arg parse that this is optional, both are recognized and equivalent
action = 'store_true'

parser.add_argument('-p','--processors', help = 'Print number of processors (default = simple output)', action = 'store_true') #shows arg parse that this is optional, both are recognized and equivalent
action = 'store_true'

parser.add_argument('-w','--walltime', help = 'Print walltime (default = simple output)', action = 'store_true') #shows arg parse that this is optional, both are recognized and equivalent
action = 'store_true'
# parse the actual arguments
# access argument values via 'args' variable
args = parser.parse_args() 

# print the number of nodes
if args.job == job_name :
    if args.nodes:
        print('#SBATCH --nodes=', args.job, 'is:' + str(nodes))

    # print the queue
    if args.queue:
        print('#SBATCH --partition', args.job, 'is:', queue)

    # print the number of processors
    if args.processors:
        print('#SBATCH --tasks-per-node=', args.job, 'is:' + str(number_of_processors))

    # print walltime
    if args.walltime:
        print('#SBATCH --time=', args.job, 'is:'  + str(walltime) + ':00:00')
else:
    print('invalid job_name')
    