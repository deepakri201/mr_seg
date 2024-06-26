# run_apply_color_table_commands.py 
# 
# Run these commands directly in the python console in Slicer, to change the colors of the 
# segmentations with the appropriate color table. 
# 
# The colors of the regions match across different methods! As closely as possible. 
# 
# Deepa Krishnaswamy 
# Brigham and Women's Hospital
# June 2024
################################################################################

### Change to use TotalSegmentator CT colors ###

color_table_filename = '/Users/dk422/git/mr_seg/color_table_TotalSegmentator_CT.ctbl'
colorNode = slicer.util.loadColorTable(color_table_filename)

segPath = "/Users/dk422/Downloads/mri_image_water_synthseg.nii.gz"
resultNode = slicer.util.loadSegmentation(segPath, {'colorNodeID': colorNode.GetID()})

### Change to use MRSegmentator colors ### 

color_table_filename = '/Users/dk422/git/mr_seg/color_table_MRSegmentator.ctbl'
colorNode = slicer.util.loadColorTable(color_table_filename)

segPath = "/Users/dk422/Downloads/mri_image_water_seg.nii.gz"
resultNode = slicer.util.loadSegmentation(segPath, {'colorNodeID': colorNode.GetID()})


