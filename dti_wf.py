
from nipype import config
config.enable_debug_mode()

import os
import eddy_node_copy as ed
import topup_node as tp
import dtifit_node as df
from nipype import SelectFiles, Node, MapNode, Workflow

# Set up working directory
homeDir = os.path.abspath('/share/foxlab-backedup/necfdg/nipype_testing/')
requestedPath = os.path.join(homeDir, 'eddy')
workingdir = os.path.realpath(requestedPath)
if not os.path.exists(workingdir):
        os.makedirs(workingdir)

# Set up image directory
imagedir = os.path.join(homeDir + '/' + 'data')

# Create SelectFiles node
templates = {'input1':'ds_*/dti_*_dwi_FH_1shell_b1200.nii',
	     'input2':'ds_*/dti_*_dwi_HF_1shell_b1200.nii'}
sf = Node(SelectFiles(templates),
          name='selectfiles', run_without_submitting=True)

# Location of the dataset folder
sf.inputs.base_directory = imagedir

# Create EddyTask nodes
eddy_in1 = MapNode(ed.EddyTask(param='0'), 
	       name='eddy_input1', iterfield=['input_file'])
eddy_in2 = MapNode(ed.EddyTask(param='0'), 
               name='eddy_input2', iterfield=['input_file'])  

# Create TopupTask node that pairs up in_file1 and in_file2 to run
topup = MapNode(tp.TopupTask(), name='topup_node', iterfield=['in_file1', 'in_file2'])   # FIX IT

# Create DtifitTask node 
dtifit = MapNode(df.DtifitTask(), name='dtifit_node', iterfield=['in_file'])

# Set up workflow
edwf = Workflow(name='my_workflow', base_dir=workingdir) 

# Connect nodes
edwf.connect(sf, 'input1', eddy_in1, 'input_file')
edwf.connect(sf, 'input2', eddy_in2, 'input_file')
edwf.connect(eddy_in1, 'output_file', topup, 'in_file1')
edwf.connect(eddy_in2, 'output_file', topup, 'in_file2')
edwf.connect(topup, 'output_file', dtifit, 'in_file')

#Run workflow
edwf.run(plugin='SLURMGraph', plugin_args={'dont_resubmit_completed_jobs':True,'template':'/share/foxlab-backedup/necfdg/nipype_testing/yizi_submit.slurm'})
