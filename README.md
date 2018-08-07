# neuroImagingPipeline

Using Nipype for creating a pipeline for DTI processing steps.

Nipype Tutorial:
- https://miykael.github.io/nipype_tutorial/ 
- http://miykael.github.io/nipype-beginner-s-guide/

How to Wrap a Cmd Line Tool Using Nipype:
- https://nipype.readthedocs.io/en/latest/devel/cmd_interface_devel.html

dti_wf.py: creating an overarching pipeline to connect steps in the DTI process 
how_to_dti.txt: containing commands for DTI steps that need to be translated and wrapped up using Nipype

eddy: 
  - eddy_node.py: wrapping cmd line tool 'eddy_correct'
  
topup:
  - topup_node.py: wrapping cmd line tool 'topup'
  
ants:
  - ants_wf.py: creating registration template for T1 images using ANTS nipype interface
  - ANTSBuildTemplate.py: ANTS nipype interface
  
