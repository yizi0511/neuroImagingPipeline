# neuroImagingPipeline

Using Nipype for creating a pipeline for DTI processing steps.

Nipype Tutorial:
- https://miykael.github.io/nipype_tutorial/ 
- http://miykael.github.io/nipype-beginner-s-guide/

How to Wrap a Cmd Line Tool Using Nipype:
- https://nipype.readthedocs.io/en/latest/devel/cmd_interface_devel.html

==============================================================================================================

__dti_wf.py:__ creating an overarching pipeline to connect steps in the DTI process 

__how_to_dti.txt:__ containing commands for DTI steps that need to be translated and wrapped up using Nipype

__eddy folder:__ 
  - eddy_node.py: wrapping cmd line tool 'eddy_correct'
  
__topup folder:__
  - topup_node.py: wrapping cmd line tool 'topup'
  
__ants folder:__
  - ants_wf.py: creating registration template for T1 images using ANTS nipype interface
  - ANTSBuildTemplate.py: ANTS nipype interface
  
