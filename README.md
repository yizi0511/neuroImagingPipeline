# neuroImagingPipeline

Using Nipype for creating a pipeline for DTI processing steps.

Nipype Tutorial:
- https://miykael.github.io/nipype_tutorial/ 
- http://miykael.github.io/nipype-beginner-s-guide/

How to Wrap a Cmd Line Tool Using Nipype:
- https://nipype.readthedocs.io/en/latest/devel/cmd_interface_devel.html

====================================================================

__dti_wf.py:__ creating an overarching pipeline to connect steps in the DTI process 

__how_to_dti.txt:__ containing commands for DTI steps that need to be translated and wrapped up using Nipype

__eddy folder:__ 
  - __eddy_node.py:__ wrapping cmd line tool 'eddy_correct'
  
__topup folder:__
  - __topup_node.py:__ wrapping cmd line tool 'topup'
  
__ants folder:__
  - __ants_wf.py:__ creating registration template for T1 images using ANTS nipype interface
  - __ANTSBuildTemplate.py:__ ANTS nipype interface
  
