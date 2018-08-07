'''
Custom eddy_correct cmd line interface 
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

# Create my own custom command line interface
# new file name ends w/ "_eddy.nii"
class EddyInputSpec(CommandLineInputSpec):
	input_file = File(desc='file to be eddy corrected', exists=True, 
			  mandatory=True, position=0, argstr="%s")
	new_file = File(desc='new file name', argstr='%s', 
		        name_source=['input_file'], 
			name_template='%s_eddy.nii', position=1)
	param = traits.Str(desc = 'Additional parameters to the command', position=2, argstr="%s")


class EddyOutputSpec(TraitedSpec):
	output_file = File(desc='eddy corrected file', exists=True)


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


