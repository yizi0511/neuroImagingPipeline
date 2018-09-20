#!/bin/sh
#
#SBATCH --job-name=YIZI_ANTS # Job name
#SBATCH --array=1
#SBATCH --nodes=1
#SBATCH --ntasks=1 # Number of cores
#SBATCH --mail-type=BEGIN # Type of email notification- BEGIN,END,FAIL,ALL
#SBATCH --mail-user=yizzhang@ucdavis.edu # Email to which notification will be sent
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=50000

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS0/out_Warp.nii.gz 01out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS1/out_Warp.nii.gz 02out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS2/out_Warp.nii.gz 03out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS3/out_Warp.nii.gz 04out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS4/out_Warp.nii.gz 05out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS5/out_Warp.nii.gz 06out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS6/out_Warp.nii.gz 07out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS7/out_Warp.nii.gz 08out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS8/out_Warp.nii.gz 09out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS9/out_Warp.nii.gz 10out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS10/out_Warp.nii.gz 11out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS11/out_Warp.nii.gz 12out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS12/out_Warp.nii.gz 13out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS13/out_Warp.nii.gz 14out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS14/out_Warp.nii.gz 15out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS15/out_Warp.nii.gz 16out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS16/out_Warp.nii.gz 17out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS17/out_Warp.nii.gz 18out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS18/out_Warp.nii.gz 19out_jacobian.nii.gz

CreateJacobianDeterminantImage 3 /share/foxlab-backedup/necfdg/nipype_testing/antsTest/ANTSTemplateBuilder/ANTSTemplateBuildSingleIterationWF_iteration04/BeginANTS/mapflow/_BeginANTS19/out_Warp.nii.gz 20out_jacobian.nii.gz


