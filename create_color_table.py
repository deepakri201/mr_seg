# create_color_table.py 
# 
# This script is to be run using Slicer. It creates a color table that can be used for 
# displaying TotalSegmentator segmentations. This is to be used when you want each 
# segmentation to be the same color across different subjects. 
# 
# To run on Mac: 
# /Applications/Slicer 4.app/Contents/MacOS/Slicer --no-splash --no-main-window --python-script "/Users/dk422/git/mr_seg/create_color_table.py" 
# 
# Deepa Krishnaswamy 
# Brigham and Women's Hospital 
# June 2024 
###################################################################################

color_table_filename_TS_CT = '/Users/dk422/git/mr_seg/color_table_TotalSegmentator_CT.ctbl'

# We create the following two manually, after we create the above table automatically.
# color_table_filename_TS_MR = '/Users/dk422/git/mr_seg/color_table_TotalSegmentator_MR.ctbl'
# color_table_filename_MRSeg = '/Users/dk422/git/mr_seg/color_table_MRSegmentator.ctbl'

###################################################################################

import glob
import os
import io
import requests

try:
    import pandas as pd
except ModuleNotFoundError:
    if slicer.util.confirmOkCancelDisplay("This module requires 'pandas' Python package. Click OK to install it now."):
        slicer.util.pip_install("pandas")
        import pandas as pd
    
try:
    import totalsegmentator 
except ModuleNotFoundError:
    if slicer.util.confirmOkCancelDisplay("This module requires 'totalsegmentator' Python package. Click OK to install it now."):
        # slicer.util.pip_install("totalsegmentator")
        slicer.util.pip_install("TotalSegmentator")
        import totalsegmentator

###################################################################################

print('creating TotalSegmentator CT colortable')

# Create a list of colors, of length of label list: 
# Labels from TotalSegmentator
labels_ts = [1,2,3,4,5,6,10,11,12,18,19,20,21,22,23,24,25,55,56,57,90,91,92,94,95,96,97,98,99,100,101,102,103]

# Get the names and label ids from the TotalSegmentator map to binary
from totalsegmentator.map_to_binary import class_map
# url = 'https://raw.githubusercontent.com/wasserth/TotalSegmentator/master/totalsegmentator/map_to_binary.py'
# download = requests.get(url).content
# # Reading the downloaded content and turning it into a pandas dataframe
# # class_map = pd.read_csv(io.StringIO(download.decode('utf-8')))
# class_map = pd.read_csv(io.StringIO(str(download,'utf-8')))
# print (class_map.head())
total_v1 = class_map['total_v1']
total_label_names = list(total_v1.keys())
labels_names = [total_v1[key] for key in labels_ts]

labels_ts_df = pd.DataFrame()
labels_ts_df['label_id'] = labels_ts 
labels_ts_df['label_name'] = labels_names

# Get the colors from the new TotalSegmentator file 
snomed_mapping_ts_file = "/Users/dk422/git/mr_seg/totalsegmentator_snomed_mapping_with_partial_colors.csv" 
snomed_mapping_ts_df = pd.read_csv(snomed_mapping_ts_file)

# Join the names on the map to binary colors to get list of colors 
# labels_ts_df_merged = pd.join([labels_ts_df, snomed_mapping_ts_df], )
labels_ts_df_merged = pd.merge(labels_ts_df, snomed_mapping_ts_df, how='left', left_on=['label_name'], right_on=['Structure'])
labels_ts_df_merged = labels_ts_df_merged[['label_id', 'label_name', 'recommendedDisplayRGBValue']]

# Form the color table file from the dataframe 
color_table_df = pd.DataFrame()
color_table_df['label_id'] = labels_ts_df_merged['label_id']
color_table_df['label_name'] = labels_ts_df_merged['label_name']
rgb = labels_ts_df_merged['recommendedDisplayRGBValue'].values 
r_list = []; b_list = []; g_list = []; last_col_list = [] 

for n in range(0,len(rgb)): 
    print(n)
    val = rgb[n]
    print(val)
    # val =  val[1:-2] # remove brackets
    val =  val[1:-1]
    print(val)
    val_array = val.split(',')
    r_list.append(int(val_array[0])) 
    g_list.append(int(val_array[1]))
    b_list.append(int(val_array[2]))
    last_col_list.append(255)

color_table_df['R'] = r_list 
color_table_df['G'] = g_list 
color_table_df['B'] = b_list
color_table_df['last_col'] = last_col_list

# Insert background as first row 
color_table_df.loc[-1] = [0, 'Background', 0, 0, 0, 0] # adding row
color_table_df.index = color_table_df.index + 1 # shifting index 
color_table_df.sort_index(inplace=True)

# Save color table 
color_table_df.to_csv(color_table_filename_TS_CT, header=None, index=None, sep=' ', mode='w')
