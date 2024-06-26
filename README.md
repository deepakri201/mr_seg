# Evaluation of AI methods for MRI segmentation on IDC data

This repository holds our Colab notebooks for evaluation of AI MR segmentation methods on IDC data for PW 41. 

See our page here: https://projectweek.na-mic.org/PW41_2024_MIT/Projects/EvaluationOfAiMethodsForMriSegmentationOnIdcData/

Methods: 
1. MRSegmentator: [paper](https://arxiv.org/pdf/2405.06463) and [code](https://github.com/hhaentze/MRSegmentator) and our [WIP colab notebook](https://github.com/deepakri201/mr_seg/blob/main/MRSegmentator_on_IDC_data_installing_python3_11_env.ipynb)
2. TotalSegmentator MRI: [paper](https://arxiv.org/pdf/2405.19492) and [code](https://github.com/wasserth/TotalSegmentator)
3. MRISegmentator-Abdomen: [paper](https://arxiv.org/pdf/2405.05944)
4. TotalVibeSegmentator: [paper](https://arxiv.org/pdf/2406.00125) and[code](https://github.com/robert-graf/TotalVibeSegmentator) and our [WIP colab notebook](https://github.com/deepakri201/mr_seg/blob/main/TotalVibeSegmentator_on_IDC_data.ipynb)

Utility code: 
- We created three color table files so that we could compare our segmentation methods. By applying these to segmentations, we ensure the segments with similar names/anatomy are displayed in the same colors. The code to [create color table files is here](https://github.com/deepakri201/mr_seg/blob/main/create_color_table.py) and code to [apply the color table to the segmentation is here](https://github.com/deepakri201/mr_seg/blob/main/run_apply_color_table_commands.py):
   1. [Color table for TotalSegmentator (v1) CT](https://github.com/deepakri201/mr_seg/blob/main/color_table_TotalSegmentator_CT.ctbl)
   2. [Color table for TotalSegmentator MRI](https://github.com/deepakri201/mr_seg/blob/main/color_table_TotalSegmentator_MRI.ctbl)
   3. [Color table for MRSegmentator](https://github.com/deepakri201/mr_seg/blob/main/color_table_MRSegmentator.ctbl)

Notes: 
- The Colab python environment is 3.10, but MRSegmentator needs python 3.11. We install 3.11 in the notebook and are able to run inference successfully. 
- We are able to run inference successfully for TotalVibeSegmentator. 

Cosmin Ciausu, Deepa Krishnaswamy, Megha Kalia, Andrey Fedorov

Brigham and Women's Hospital 

June 2024 

