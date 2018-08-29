#!/bin/bash

# This is a bash file... 

# echo $0
# echo "this is the first commandline argument: "$1
# echo "this is the second commandline argument: "$2

input_file=$1
output_file=$2

prefix=${input_file/.nii.gz/}

#module load java/jdk1.8.0_05

export CAMINO_HEAP_SIZE=3000
echo fslmaths $1 -mas ${prefix}_strip_mask.nii.gz ${prefix}_strip.nii.gz
fslmaths $1 -mas ${prefix}_strip_mask.nii.gz ${prefix}_strip.nii.gz
# echo gunzip -f ${prefix}_strip.nii.gz 
gunzip -f -q ${prefix}_strip.nii.gz 
echo image2voxel -4dimage ${prefix}_strip.nii > ${prefix}_DWI.Bfloat
image2voxel -4dimage ${prefix}_strip.nii > ${prefix}_DWI.Bfloat
modelfit -inputfile ${prefix}_DWI.Bfloat -schemefile necfdg_schemefile.scheme -outputdatatype float > ${prefix}_DTI.Bfloat
dt2nii -inputfile ${prefix}_DTI.Bfloat -inputdatatype float -header ${prefix}_strip.nii -outputroot $output_file
gzip -fq ${prefix}_strip.nii

