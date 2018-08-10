from __future__ import print_function, unicode_literals
from builtins import open
from future import standard_library
standard_library.install_aliases()

from nipype import config
config.enable_debug_mode()

"""
==================================================
Using ANTS for creating a T1 registration template
==================================================

We will use ANTS based workflow to create a template out of multiple T1 volumes.
We will use NMT.nii as the starting template.
We will run 4 iterations of ANTS template builder workflow to average the T1 images. 
The original ANTSTemplateBuildSingleIterationWF processes passive T1 images 
but we will ignore this process for the sake of convenience.

IMPORTANT:
I hardcoded the nipype interface 'nipype.workflows.smri.ants.ANTSBuildTemplate'
in order to tweak the parameters to fit monkeys' brains. The changed version of
'nipype.workflows.smri.ants.ANTSBuildTemplate' is included in ants directory
for your reference. Hardcoding is not recommended. If you have better ways to
change the parameters of ANTS please do so. 

I only changed BeginANTS node of ANTSBuildTemplate workflow so that the desired 
cmd line command would be:
'ANTS 3 -m PR[reference.nii,input.nii,1,2] -i 30x20x20x5 -r Gauss[2,0] -t SyN[.25] -o output.nii'

Pathway for ANTSBuildTemplate.py:
/share/foxlab-backedup/apps/conda/lib/python3.6/site-packages/nipype/workflows/smri/ants/ANTSBuildTemplate.py
"""

"""
1. Tell python where to find the appropriate functions
	ANTSBuildTemplate uses ANTS interface instead of the new Registration interface in nipype
"""
import os
import nipype.interfaces.utility as util
import nipype.interfaces.ants as ants
import nipype.interfaces.io as io
import nipype.pipeline.engine as pe  
from nipype.workflows.smri.ants.ANTSBuildTemplate import ANTSTemplateBuildSingleIterationWF

"""
2. Set up image directory and working directory. Define input images
	01_T1_half.nii.gz taken from ~/mri/*/T1_masked_LPI.nii.gz 
"""
workingdir = os.path.abspath('/share/foxlab-backedup/necfdg/nipype_testing/antsTest')
imagedir = os.path.abspath('/share/foxlab-backedup/necfdg/nipype_testing/image')

input_images = [
    os.path.join(imagedir, '01_T1_half.nii.gz'),
    os.path.join(imagedir, '02_T1_half.nii.gz'),
    os.path.join(imagedir, '03_T1_half.nii.gz'),
    os.path.join(imagedir, '04_T1_half.nii.gz'),
    os.path.join(imagedir, '05_T1_half.nii.gz'),
    os.path.join(imagedir, '06_T1_half.nii.gz'),
    os.path.join(imagedir, '07_T1_half.nii.gz'),
    os.path.join(imagedir, '08_T1_half.nii.gz'),
    os.path.join(imagedir, '09_T1_half.nii.gz'),
    os.path.join(imagedir, '10_T1_half.nii.gz'),
    os.path.join(imagedir, '11_T1_half.nii.gz'),
    os.path.join(imagedir, '12_T1_half.nii.gz'),
    os.path.join(imagedir, '13_T1_half.nii.gz'),
    os.path.join(imagedir, '14_T1_half.nii.gz'),
    os.path.join(imagedir, '15_T1_half.nii.gz'),
    os.path.join(imagedir, '16_T1_half.nii.gz'),
    os.path.join(imagedir, '17_T1_half.nii.gz'),
    os.path.join(imagedir, '18_T1_half.nii.gz'),
    os.path.join(imagedir, '19_T1_half.nii.gz'),
    os.path.join(imagedir, '20_T1_half.nii.gz')
]

"""
3. Define ANTS workflow
"""
tbuilder = pe.Workflow(name="ANTSTemplateBuilder")
tbuilder.base_dir = workingdir

"""
4. Define data sources
"""
datasource = pe.Node(interface=util.IdentityInterface(fields=['imageList', 'initTemp']),
   		     run_without_submitting=True, name='inputT1Images')
datasource.inputs.imageList = input_images
<<<<<<< HEAD
datasource.inputs.initTemp = os.path.join(imagedir, 'NMT.nii.gz') 
=======
datasource.inputs.initTemp = os.path.join(imagedir + 'NMT.nii.gz') 
>>>>>>> 4215c2ef27186d8a91c97c445e47fde358c6518d
datasource.inputs.sort_filelist = True

"""
5. Define the first iteration of template building
"""
buildTemplateIteration1 = ANTSTemplateBuildSingleIterationWF('iteration01')
tbuilder.connect(datasource, 'initTemp', buildTemplateIteration1,
                 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration1,
                 'inputspec.images')

"""
6. Define the second iteration of template building
"""

buildTemplateIteration2 = ANTSTemplateBuildSingleIterationWF('iteration02')
tbuilder.connect(buildTemplateIteration1, 'outputspec.template',
                 buildTemplateIteration2, 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration2,
                 'inputspec.images')

"""
7. Define the third iteration of template building
"""

buildTemplateIteration3 = ANTSTemplateBuildSingleIterationWF('iteration03')
tbuilder.connect(buildTemplateIteration2, 'outputspec.template',
                 buildTemplateIteration3, 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration3,
                 'inputspec.images')

"""
8. Define the fourth iteration of template building
"""

buildTemplateIteration4 = ANTSTemplateBuildSingleIterationWF('iteration04')
tbuilder.connect(buildTemplateIteration3, 'outputspec.template',
                 buildTemplateIteration4, 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration4,
                 'inputspec.images')

"""
9. Move output files to a designated results folder
"""
datasink = pe.Node(io.DataSink(), name="datasink")
datasink.inputs.base_directory = os.path.join(workingdir, "antResults")
tbuilder.connect(buildTemplateIteration4, 'outputspec.template', datasink,
                 'antsTemplate')

"""
10. Run ANTS workflow
	write_graph(): generate workflow graph
	plugin options: 'SLURM' or 'SLURMGraph'
"""
tbuilder.write_graph(graph2use='exec', format='png', simple_form=False)
tbuilder.run(plugin='SLURMGraph', plugin_args={'dont_resubmit_completed_jobs':True, 'template':'/share/foxlab-backedup/necfdg/nipype_testing/yizi_submit.slurm'})

