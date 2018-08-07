'''
Custom topup cmd line interface that prints below cmd:

./create_dti_topup.sh /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_006_dwi_HF_1shell_b1200_eddy.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup.nii

'''

# Import nipype interfaces
from nipype.interfaces.base import (
        TraitedSpec,
        CommandLineInputSpec,
        CommandLine,
        File,
        traits
)
from nipype.utils.filemanip import split_filename
import os


# Create my own custom cmd line interface
class TopupInputSpec(CommandLineInputSpec):
	in_file1 = File(desc='1st input file', exists=True,
			   mandatory=True, position=0, argstr='%s')
	in_file2 = File(desc='2nd input file', exists=True,
			   mandatory=True, position=1, argstr='%s')
	out_file = File(desc='output file after topup', position=2, argstr='%s',
			name_source=['in_file1'],
			name_template='%s_topup.nii')

class TopupOutputSpec(TraitedSpec):
	output_file = File(desc='file after topup', exists=True)

class TopupTask(CommandLine):
	input_spec = TopupInputSpec
	output_spec = TopupOutputSpec
	_cmd = '/share/foxlab-backedup/necfdg/nipype_testing/topup/create_dti_topup.sh'

	#def _format_arg(self, opt, spec, val):
	#	if opt == 'out_file':
	#		dirname = os.path.dirname(self.inputs.in_file1)
	#		_, prefix = os.path.split(dirname)
	#		val = prefix + '_' + val
	#	return super(TopupTask, self)._format_arg(opt, spec, val)

	def _list_outputs(self):
		path, fname, ext = split_filename(self.inputs.in_file1)
		#_, prefix = os.path.split(path)
		outputs = self.output_spec().get()
		outputs['output_file'] = os.path.abspath(fname + '_topup.nii.gz')
		return outputs  




