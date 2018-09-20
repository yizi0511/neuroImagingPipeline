#!/bin/sh
#
#SBATCH --job-name=YIZI_ANTS # Job name
#SBATCH --array=1
#SBATCH --nodes=1
#SBATCH --ntasks=1 # Number of cores
#SBATCH --mail-type=BEGIN # Type of email notification- BEGIN,END,FAIL,ALL
#SBATCH --mail-user=yizzhang@ucdavis.edu # Email to which notification will be sent
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=50000

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/01_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 01_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/01_T1_half.nii.gz 01_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 01_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/02_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 02_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/02_T1_half.nii.gz 02_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 02_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/03_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 03_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/03_T1_half.nii.gz 03_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 03_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/04_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 04_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/04_T1_half.nii.gz 04_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 04_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/05_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 05_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/05_T1_half.nii.gz 05_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 05_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/06_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 06_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/06_T1_half.nii.gz 06_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 06_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/07_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 07_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/07_T1_half.nii.gz 07_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 07_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/08_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 08_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/08_T1_half.nii.gz 08_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 08_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/09_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 09_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/09_T1_half.nii.gz 09_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 09_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/10_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 10_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/10_T1_half.nii.gz 10_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 10_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/11_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 11_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/11_T1_half.nii.gz 11_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 11_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/12_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 12_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/12_T1_half.nii.gz 12_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 12_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/13_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 13_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/13_T1_half.nii.gz 13_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 13_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/14_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 14_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/14_T1_half.nii.gz 14_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 14_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/15_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 15_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/15_T1_half.nii.gz 15_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 15_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/16_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 16_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/16_T1_half.nii.gz 16_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 16_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/17_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 17_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/17_T1_half.nii.gz 17_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 17_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/18_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 18_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/18_T1_half.nii.gz 18_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 18_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/19_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 19_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/19_T1_half.nii.gz 19_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 19_out_Affine.txt

ANTS 3 -m MI[/share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz, /share/foxlab-backedup/necfdg/nipype_testing/image/20_T1_half.nii.gz, 1,2] -i 0 --rigid-affine true -o 20_out_
WarpImageMultiTransform 3 /share/foxlab-backedup/necfdg/nipype_testing/image/20_T1_half.nii.gz 20_T1_half_wimt.nii.gz -R /share/foxlab-backedup/necfdg/nipype_testing/image/NMT_SS.nii.gz 20_out_Affine.txt


