# neuroImagingPipeline

Using Nipype to create a pipeline for DTI processing steps.

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
  - __topup_node.py:__ wrapping cmd line executable 'create_dti_topup.sh'
  - __create_dti_topup.sh:__ cmd line executable that runs 'topup' on subjects
  - __dti_topup_params.txt:__ file needed by create_dti_topup.sh
  
__dtitf folder:__
  - __dtitf_node.py:__ wrapping cmd line executable 'lil_dtifit.sh'
  - __lil_dtifit.sh:__ cmd line executable that runs DTIFIT on subjects
  - __necfdg_schemefile.scheme:__ file needed by lil_dtifit.sh
  
__ants folder:__
  - __ants_wf.py:__ creating registration template for T1 images using ANTS nipype interface
  - __ANTSBuildTemplate.py:__ ANTS nipype interface
  - __preANTS_cmd.slurm:__ bash cmd that runs linear transform only on subjects (do this before running ANTS workflow) 
  - __JacobianDeform.slurm:__ bash cmd that finds Jacobian deformation field of the images (do this after running ANTS)
  - __smoothing.slurm:__ bash cmd that smoothes the Jacobian deformation field images
  - __NMT_SS.nii.gz:__ initial template for ANTS workflow (stripped skull)
  - __ANTSwfinfo.txt:__ contains important info about subject ID 
  
