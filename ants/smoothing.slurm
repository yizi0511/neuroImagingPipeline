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


SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/01out_jacobian.nii.gz -fwhm 4 4 4 -out 01out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/02out_jacobian.nii.gz -fwhm 4 4 4 -out 02out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/03out_jacobian.nii.gz -fwhm 4 4 4 -out 03out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/04out_jacobian.nii.gz -fwhm 4 4 4 -out 04out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/05out_jacobian.nii.gz -fwhm 4 4 4 -out 05out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/06out_jacobian.nii.gz -fwhm 4 4 4 -out 06out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/07out_jacobian.nii.gz -fwhm 4 4 4 -out 07out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/08out_jacobian.nii.gz -fwhm 4 4 4 -out 08out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/09out_jacobian.nii.gz -fwhm 4 4 4 -out 09out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/10out_jacobian.nii.gz -fwhm 4 4 4 -out 10out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/11out_jacobian.nii.gz -fwhm 4 4 4 -out 11out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/12out_jacobian.nii.gz -fwhm 4 4 4 -out 12out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/13out_jacobian.nii.gz -fwhm 4 4 4 -out 13out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/14out_jacobian.nii.gz -fwhm 4 4 4 -out 14out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/15out_jacobian.nii.gz -fwhm 4 4 4 -out 15out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/16out_jacobian.nii.gz -fwhm 4 4 4 -out 16out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/17out_jacobian.nii.gz -fwhm 4 4 4 -out 17out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/18out_jacobian.nii.gz -fwhm 4 4 4 -out 18out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/19out_jacobian.nii.gz -fwhm 4 4 4 -out 19out_jacobian_4mm.nii.gz

SVGaussianSmoothing -in /share/foxlab-backedup/necfdg/nipype_testing/ants/20out_jacobian.nii.gz -fwhm 4 4 4 -out 20out_jacobian_4mm.nii.gz

