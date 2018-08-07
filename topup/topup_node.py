"""
===================================
Custom cmd line interface for topup
===================================

The desired cmd line output:

./create_dti_topup.sh /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_006_dwi_HF_1shell_b1200_eddy.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup.nii
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
	Remember to specify the path of the executable 'create_dti_topup.sh'
"""
class TopupInputSpec(CommandLineInputSpec):
	in_file1 = File(desc='input file 1', exists=True,
			   mandatory=True, position=0, argstr='%s')
	in_file2 = File(desc='input file 2', exists=True,
			   mandatory=True, position=1, argstr='%s')
	out_file = File(desc='output file name', position=2, argstr='%s',
			name_source=['in_file1'],
			name_template='%s_topup.nii')

class TopupOutputSpec(TraitedSpec):
	output_file = File(desc='output file after topup', exists=True)

class TopupTask(CommandLine):
	input_spec = TopupInputSpec
	output_spec = TopupOutputSpec
	_cmd = '/share/foxlab-backedup/necfdg/nipype_testing/topup/create_dti_topup.sh'

	def _list_outputs(self):
		path, fname, ext = split_filename(self.inputs.in_file1)
		outputs = self.output_spec().get()
		outputs['output_file'] = os.path.abspath(fname + '_topup.nii.gz')
		return outputs  




