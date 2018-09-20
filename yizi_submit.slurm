#!/bin/sh
#
#SBATCH --job-name=YIZI_ANTS # Job name
#SBATCH --array=1
#SBATCH --nodes=1
#SBATCH --ntasks=1 # Number of cores
#SBATCH --mail-type=BEGIN # Type of email notification- BEGIN,END,FAIL,ALL
#SBATCH --mail-user=yizzhang@ucdavis.edu # Email to which notification will be sent
#SBATCH --time=96:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=50000

which ANTS
