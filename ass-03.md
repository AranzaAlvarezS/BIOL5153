BIOL5153
Dr. Alverson
10/03
Assignment 3

1. **Uploading mt_genomes directory onto the AHPCC:**
`rsync -r mt_genomes aranzaa@hpc-portal2.hpc.uark.edu:/storage/aranzaa/`

2.**Uploading mt_genomes directory onto the AHPCC:**
`scp unknown.fa aranzaa@hpc-portal2.hpc.uark.edu:/storage/aranzaa/mt_genomes`

3. **Writimg a SLURM script:** 
`nano ass_3_job.slurm`

**SLURM script**
#!/bin/bash

#SBATCH --job-name=assignment_3
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=1
#SBATCH --time= 0:05:00
#SBATCH -o test_%j.out
#SBATCH -e test_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=aranzaa@uark.edu


module purge
modle load blast/2.3.0+

cd $SLURM_SUBMIT_DIR
cat *.fasta > genomes.fas

makeblastdb -in genomes.fas -dbtype nucl

blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn

**Commands to run SLURM script and submit job**
`qstat -q`
`sbatch ass_3_job.slurm`
`qstat | grep aranzaa`
`ls -al`
`less unknown.vs.genomes.blastn`

4. **Synchronozing the remote mt_gemomes**
`rsync -r mt_genomes aranzaa@hpc-portal2.hpc.uark.edu:/storage/aranzaa/`

5. **Answer Questions:**
How long did it take your job to complete?
Less than 1 sec.

What is the closest match to the database?
Curcubita

Can you tell from the coordinates which gene is unknown.fa?
cox 1 gene from Lufa

6. **Pushing assignment 3 into repository:**
`git add ass-03.md`
`git status`
`git commit -m "added assignment 3"`
`git push -u origin main`

