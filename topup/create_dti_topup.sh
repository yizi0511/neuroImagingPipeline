#!/bin/bash

input1=$1
input2=$2
output=$3
input_prefix=${input1/\.nii/}
input_prefix=${input_prefix/\.gz/}
input_prefix=${input_prefix}_forTopup

output_prefix=${output/\.nii/}
output_prefix=${output_prefix/\.gz/}
output_prefix=${output_prefix}_forTopup

echo $input_prefix
echo $output_prefix


fslroi $input1 ${input_prefix}_1_1 0 1 
fslroi $input1 ${input_prefix}_1_2 12 1
fslroi $input1 ${input_prefix}_1_3 23 1
fslroi $input1 ${input_prefix}_1_4 34 1
fslroi $input1 ${input_prefix}_1_5 45 1
fslroi $input1 ${input_prefix}_1_6 56 1
fslroi $input1 ${input_prefix}_1_7 67 1


fslroi $input2 ${input_prefix}_2_1 0 1 
fslroi $input2 ${input_prefix}_2_2 12 1
fslroi $input2 ${input_prefix}_2_3 23 1
fslroi $input2 ${input_prefix}_2_4 34 1
fslroi $input2 ${input_prefix}_2_5 45 1
fslroi $input2 ${input_prefix}_2_6 56 1
fslroi $input2 ${input_prefix}_2_7 67 1

fslmerge -t ${input_prefix}_merged ${input_prefix}_?_1.nii.gz 


topup --imain=${input_prefix}_merged.nii.gz --datain=/share/foxlab-backedup/necfdg/nipype_testing/topup/dti_topup_params.txt --config=b02b0.cnf --out=${output_prefix}
applytopup --imain=$input1,$input2 --inindex=1,2 --datain=/share/foxlab-backedup/necfdg/nipype_testing/topup/dti_topup_params.txt --topup=${output_prefix} --out=${output}




