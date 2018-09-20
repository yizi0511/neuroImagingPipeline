"""
=============================================================
Using nipype for creating a pipeline for DTI processing steps
=============================================================  
"""

"""
1. Tell python where to find the appropriate functions
	eddy_node.py: a custom cmd line wrapper for eddy correction
	topup_node.py: a custom cmd line wrapper for topup
"""
from nipype import config		
config.enable_debug_mode()

import os
from nipype import SelectFiles, Node, MapNode, Workflow
import eddy_node as ed		
import topup_node as tp
import bet_node as bt
import dtitf_node as tf

"""
2. Set up image directory and working directory 
"""
workingdir = os.path.abspath('/share/foxlab-backedup/necfdg/nipype_testing')
imagedir = os.path.abspath('/share/foxlab-backedup/necfdg/nipype_testing/data')

"""
3. Define data sources. Using SelectFiles interface to import images from image directory
"""
templates = {'input1':'ds_*/dti_*_dwi_FH_1shell_b1200.nii',
	     'input2':'ds_*/dti_*_dwi_HF_1shell_b1200.nii'}
sf = Node(SelectFiles(templates), name='selectfiles', run_without_submitting=True)
sf.inputs.base_directory = imagedir

"""
4. Define eddy correction step
"""
eddy_in1 = MapNode(ed.EddyTask(param='0'), 
	       name='eddy_input1', iterfield=['input_file'])
eddy_in2 = MapNode(ed.EddyTask(param='0'), 
               name='eddy_input2', iterfield=['input_file'])  

"""
5. Define topup step
"""
topup = MapNode(tp.TopupTask(), name='topup_node', iterfield=['in_file1', 'in_file2'])   

"""
6. Define bet step
"""
bet = MapNode(bt.BetTask(param2='-f', param3='0.3', param4='-m', param5='-n'),
	name='bet_node', iterfield=['in_file'])

"""
7. Define dtifit step 
"""
dtifit = MapNode(tf.DtitfTask(), name='dtifit_node', iterfield=['in_file', 'mask_file'])

"""
8. Set up DTI workflow
"""
dtiwf = Workflow(name='dti_workflow', base_dir=workingdir) 
dtiwf.connect(sf, 'input1', eddy_in1, 'input_file')
dtiwf.connect(sf, 'input2', eddy_in2, 'input_file')
dtiwf.connect(eddy_in1, 'output_file', topup, 'in_file1')
dtiwf.connect(eddy_in2, 'output_file', topup, 'in_file2')
dtiwf.connect(topup, 'output_file', bet, 'in_file')
dtiwf.connect(topup, 'output_file', dtifit, 'in_file')
dtiwf.connect(bet, 'output_file', dtifit, 'mask_file')

"""
9. Run DTI workflow
	write_graph(): generate workflow graph 
	plugin options: 'SLURM' or 'SLURMGraph'
"""
dtiwf.write_graph(graph2use='exec', format='png', simple_form=False)
dtiwf.run(plugin='SLURMGraph', plugin_args={'dont_resubmit_completed_jobs':True,'template':'/share/foxlab-backedup/necfdg/nipype_testing/yizi_submit.slurm'})


