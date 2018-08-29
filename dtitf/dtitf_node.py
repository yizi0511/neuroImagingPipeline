"""
===================================
Custom cmd line interface for dtitf
===================================

The desired cmd line output:

./lil_dtifit.sh /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup_strip_mask.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup_

"""

"""
1. Tell python where to find the appropriate functions
"""
from nipype.interfaces.base import (
        TraitedSpec,
        CommandLineInputSpec,
        CommandLine,
        File,
        traits
)
from nipype.utils.filemanip import split_filename
import os

"""
2. Please refer to instructions in README.md for detailed description of how to wrap a cmd line tool
        _list_outputs(): aggregate output files to designated result folder so that it is 
        not stored temporarily 
	Remember to specify the path of the executable 'lil_dtifit.sh'
"""
class DtitfInputSpec(CommandLineInputSpec):
	in_file = File(desc='input file', exists=True,
			   mandatory=True, position=0, argstr='%s')
	mask_file = File(desc='strip mask file', exists=True,
			   mandatory=True, position=1, argstr='%s')
	out_file = File(desc='output file name', position=2, argstr='%s',
			name_source=['in_file'],
			name_template='%s_')

class DtitfOutputSpec(TraitedSpec):
	output_file = File(desc='output file after dtitf', exists=True)

class DtitfTask(CommandLine):
	input_spec = DtitfInputSpec
	output_spec = DtitfOutputSpec
	_cmd = '/share/foxlab-backedup/necfdg/nipype_testing/dtitf/lil_dtifit.sh'

# EDIT HERE
	def _list_outputs(self):
		path, fname, ext = split_filename(self.inputs.in_file)
		outputs = self.output_spec().get()
		outputs['output_file'] = os.path.abspath(fname + '_dt.nii.gz')
		return outputs  




