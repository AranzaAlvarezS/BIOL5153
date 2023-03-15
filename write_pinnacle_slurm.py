#! /usr/bin/env python3

#write_pinnacle_slurm
#assignment_4


#Defining variables
job_name = 'assignment_4'
queue = 'comp 72'
nodes = '1'
number_of_processors = '32'
walltime = '02:00:00'
command = 'command1'



print('#!/bin/bash')
print(' ')
print('#SBATCH --job-name=','<',job_name,'>') #job name
print('#SBATCH --partition',queue) #queue
print('#SBATCH --nodes=',nodes) #number of nodes
print('#SBATCH --tasks-per-node=',number_of_processors) #number of processors
print('#SBATCH --time=', walltime) #walltime
print('#SBATCH -o %j.out')
print('#SBATCH -e %j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=aranzaa@uark.edu')
print(' ')
print('cd $SLURM_SUBMIT_DIR')
print(' ')
print('#job command here')
print(command)



