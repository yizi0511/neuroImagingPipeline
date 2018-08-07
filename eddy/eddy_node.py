"""
=============================================
Custom cmd line interface for eddy correction
=============================================

The desired cmd line output:

eddy_correct /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200.nii /share/foxlab-backedup/necfdg/mri/ds_2017-09-26_09-00/dti_005_dwi_FH_1shell_b1200_eddy.nii 0
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
	_format_arg(): change output file name by changing the format of 'new_file' arg
	Please ask Yizi if you have confusions about what this function does
	_list_outputs(): aggregate output files to designated result folder so that it is 
	not stored temporarily 
"""
class EddyInputSpec(CommandLineInputSpec):
	input_file = File(desc='input file to be eddy corrected', exists=True, 
			  mandatory=True, position=0, argstr="%s")
	new_file = File(desc='output file name', argstr='%s', 
		        name_source=['input_file'], 
			name_template='%s_eddy.nii', position=1)
	param = traits.Str(desc = 'Additional parameter to the command', position=2, argstr="%s")


class EddyOutputSpec(TraitedSpec):
	output_file = File(desc='output file after eddy correction', exists=True)


class EddyTask(CommandLine):
	input_spec = EddyInputSpec
	output_spec = EddyOutputSpec
	_cmd = 'eddy_correct'

	def _format_arg(self, opt, spec, val):
		if opt == 'new_file':
			dirname = os.path.dirname(self.inputs.input_file)
			_, prefix = os.path.split(dirname)
			val = prefix + '_' + val
		return super(EddyTask, self)._format_arg(opt, spec, val)   		
	
	def _list_outputs(self):
		path, fname, ext = split_filename(self.inputs.input_file)
		_, prefix = os.path.split(path)
		outputs = self.output_spec().get()
		outputs['output_file'] = os.path.abspath(prefix + '_' + fname
							 + "_eddy.nii.gz")
		return outputs


