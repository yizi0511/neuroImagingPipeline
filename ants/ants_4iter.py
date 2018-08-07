"""
===============================================
sMRI: Using new ANTS for creating a T1 template
===============================================

In this tutorial we will use ANTS (old version aka "ANTS") based workflow  to
create a template out of multiple T1 volumes.

1. Tell python where to find the appropriate functions.
"""

from __future__ import print_function, unicode_literals
from builtins import open
from future import standard_library
standard_library.install_aliases()

from nipype import config
config.enable_debug_mode()

import os
import nipype.interfaces.utility as util
import nipype.interfaces.ants as ants
import nipype.interfaces.io as io
import nipype.pipeline.engine as pe  # pypeline engine

from nipype.workflows.smri.ants.ANTSBuildTemplate import ANTSTemplateBuildSingleIterationWF
"""
2. Download T1 volumes into home directory
"""

workingdir = os.path.abspath('/share/foxlab-backedup/necfdg/nipype_testing/antsTest')
mydatadir = os.path.join('/share/foxlab-backedup/necfdg/nipype_testing/image')

# 01_T1_half.nii.gz from ~/mri/*/T1_masked_LPI.nii.gz
# 01_T1_inv_half.nii.gz from ~/mri/*/T1_masked.nii.gz
input_images = [
    os.path.join(mydatadir, '01_T1_half.nii.gz'),
    os.path.join(mydatadir, '02_T1_half.nii.gz'),
    os.path.join(mydatadir, '03_T1_half.nii.gz'),
    os.path.join(mydatadir, '04_T1_half.nii.gz'),
    os.path.join(mydatadir, '05_T1_half.nii.gz'),
    os.path.join(mydatadir, '06_T1_half.nii.gz'),
    os.path.join(mydatadir, '07_T1_half.nii.gz'),
    os.path.join(mydatadir, '08_T1_half.nii.gz'),
    os.path.join(mydatadir, '09_T1_half.nii.gz'),
    os.path.join(mydatadir, '10_T1_half.nii.gz'),
    os.path.join(mydatadir, '11_T1_half.nii.gz'),
    os.path.join(mydatadir, '12_T1_half.nii.gz'),
    os.path.join(mydatadir, '13_T1_half.nii.gz'),
    os.path.join(mydatadir, '14_T1_half.nii.gz'),
    os.path.join(mydatadir, '15_T1_half.nii.gz'),
    os.path.join(mydatadir, '16_T1_half.nii.gz'),
    os.path.join(mydatadir, '17_T1_half.nii.gz'),
    os.path.join(mydatadir, '18_T1_half.nii.gz'),
    os.path.join(mydatadir, '19_T1_half.nii.gz'),
    os.path.join(mydatadir, '20_T1_half.nii.gz')
]


#input_passive_images = [{
#    'INV_T1':
#    os.path.join(mydatadir, '01_T1_inv_half.nii.gz')
#}, {
#    'INV_T1':
#    os.path.join(mydatadir, '02_T1_inv_half.nii.gz')
#}, {
#    'INV_T1':
#    os.path.join(mydatadir, '03_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '04_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '05_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '06_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '07_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '08_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '09_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '10_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '11_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '12_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '13_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '14_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '15_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '16_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '17_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '18_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '19_T1_inv_half.nii.gz')
#},{
#    'INV_T1':
#    os.path.join(mydatadir, '20_T1_inv_half.nii.gz')
#}]

"""
3. Define the workflow and its working directory
"""

tbuilder = pe.Workflow(name="ANTTemplateBuilder_4iter")
tbuilder.base_dir = workingdir
"""
4. Define data sources. In real life these would be replace by DataGrabbers
"""

datasource = pe.Node(
    interface=util.IdentityInterface(
        fields=['imageList', 'initTemp']),
    run_without_submitting=True,
    name='InputT1Images')
datasource.inputs.imageList = input_images
datasource.inputs.initTemp = os.path.join(mydatadir + '/NMT.nii.gz') 
datasource.inputs.sort_filelist = True

"""
6. Define the first iteration of template building
"""

buildTemplateIteration1 = ANTSTemplateBuildSingleIterationWF('iteration01')
tbuilder.connect(datasource, 'initTemp', buildTemplateIteration1,
                 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration1,
                 'inputspec.images')
#tbuilder.connect(datasource, 'passiveImagesDictionariesList',
#                 buildTemplateIteration1,
#                 'inputspec.ListOfPassiveImagesDictionaries')
"""
7. Define the second iteration of template building
"""

buildTemplateIteration2 = ANTSTemplateBuildSingleIterationWF('iteration02')
tbuilder.connect(buildTemplateIteration1, 'outputspec.template',
                 buildTemplateIteration2, 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration2,
                 'inputspec.images')
#tbuilder.connect(datasource, 'passiveImagesDictionariesList',
#                 buildTemplateIteration2,
#                 'inputspec.ListOfPassiveImagesDictionaries')

"""
8. Define the third iteration of template building
"""

buildTemplateIteration3 = ANTSTemplateBuildSingleIterationWF('iteration03')
tbuilder.connect(buildTemplateIteration2, 'outputspec.template',
                 buildTemplateIteration3, 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration3,
                 'inputspec.images')
#tbuilder.connect(datasource, 'passiveImagesDictionariesList',
#                 buildTemplateIteration3,
#                 'inputspec.ListOfPassiveImagesDictionaries')

"""
7. Define the fourth iteration of template building
"""

buildTemplateIteration4 = ANTSTemplateBuildSingleIterationWF('iteration04')
tbuilder.connect(buildTemplateIteration3, 'outputspec.template',
                 buildTemplateIteration4, 'inputspec.fixed_image')
tbuilder.connect(datasource, 'imageList', buildTemplateIteration4,
                 'inputspec.images')
#tbuilder.connect(datasource, 'passiveImagesDictionariesList',
#                 buildTemplateIteration4,
#                 'inputspec.ListOfPassiveImagesDictionaries')


"""
10. Move selected files to a designated results folder
"""

datasink = pe.Node(io.DataSink(), name="datasink")
datasink.inputs.base_directory = os.path.join(workingdir, "antResults_4iter")

tbuilder.connect(buildTemplateIteration4, 'outputspec.template', datasink,
                 'PrimaryTemplate')
#tbuilder.connect(buildTemplateIteration4,
#                 'outputspec.passive_deformed_templates', datasink,
#                 'PassiveTemplate')
"""
11. Run the workflow
"""
tbuilder.write_graph(graph2use='exec', format='png', simple_form=False)
tbuilder.run(plugin='SLURMGraph', plugin_args={'dont_resubmit_completed_jobs':True, 'template':'/share/foxlab-backedup/necfdg/nipype_testing/yizi_submit.slurm'})

