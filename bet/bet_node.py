"""
===================================
Custom cmd line interface for bet
===================================

The desired cmd line output:

bet /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup.nii.gz /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy_topup_strip
 -f 0.3 -m -n

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
"""
class BetInputSpec(CommandLineInputSpec):
	in_file = File(desc='input file to be stripped', exists=True,
			   mandatory=True, position=0, argstr='%s')
	out_file = File(desc='output file name', position=1, argstr='%s',
			name_source=['in_file'],
			name_template='%s_strip')
	param2 = traits.Str(desc='Additional param to the cmd', position=2, argstr='%s')
	param3 = traits.Str(desc='Additional param to the cmd', position=3, argstr='%s') 
	param4 = traits.Str(desc='Additional param to the cmd', position=4, argstr='%s') 
	param5 = traits.Str(desc='Additional param to the cmd', position=5, argstr='%s') 


class BetOutputSpec(TraitedSpec):
	output_file = File(desc='file after bet', exists=True)

class BetTask(CommandLine):
	input_spec = BetInputSpec
	output_spec = BetOutputSpec
	_cmd = 'bet'

	#def _format_arg(self, opt, spec, val):
	#	if opt == 'out_file':
	#		dirname = os.path.dirname(self.inputs.in_file1)
	#		_, prefix = os.path.split(dirname)
	#		val = prefix + '_' + val
	#	return super(TopupTask, self)._format_arg(opt, spec, val)

	def _list_outputs(self):
		path, fname, ext = split_filename(self.inputs.in_file)
		#_, prefix = os.path.split(path)
		outputs = self.output_spec().get()
		outputs['output_file'] = os.path.abspath(fname + '_strip_mask.nii.gz')
		return outputs  




