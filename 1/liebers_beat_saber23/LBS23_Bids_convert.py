# import os
# import pandas as pd

# def convert_to_bids(source_dir, destination_dir):
#     """
#     Converts multiple Parquet files into BIDS-compliant motion data TSV format for each subject.

#     Parameters:
#         source_dir (str): Path to the source directory containing the original Parquet files.
#         destination_dir (str): Path to the destination directory for BIDS-compliant files.
#     """
#     if not os.path.exists(destination_dir):
#         os.makedirs(destination_dir)
    
#     for file in os.listdir(source_dir):
#         if file.startswith("P") and file.endswith(".parquet"):  # Check for expected file naming
#             # Extract subject ID (e.g., P1 from P1_<uuid>.parquet)
#             sub_id = file.split("_")[0]
#             sub_bids = f"sub-{sub_id}"  # Convert to BIDS format
            
#             # Define paths
#             sub_dir = os.path.join(destination_dir, sub_bids, "ses-1", "motion")
#             os.makedirs(sub_dir, exist_ok=True)
            
#             # Generate unique filename for each file
#             file_uuid = file.split("_")[1].replace(".parquet", "")  # Extract UUID
#             bids_filename = f"{sub_bids}_task-behavioralbiometrics_tracksys-VR_{file_uuid}_motion.tsv"
#             bids_filepath = os.path.join(sub_dir, bids_filename)
            
#             # Convert Parquet to TSV
#             original_filepath = os.path.join(source_dir, file)
#             try:
#                 # Read Parquet file and save as .tsv
#                 df = pd.read_parquet(original_filepath)
#                 df.to_csv(bids_filepath, sep="\t", index=False)
#                 print(f"Converted: {file} -> {bids_filepath}")
#             except Exception as e:
#                 print(f"Failed to convert {file}: {e}")

# # Example usage
# source_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_orginal"
# destination_directory = r"d:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_converted"
# convert_to_bids(source_directory, destination_directory)

import os
import pandas as pd
from collections import defaultdict

def convert_to_bids(source_dir, destination_dir):
    """
    Converts Parquet files into BIDS-compliant motion data TSV format with session IDs based on unique session identifiers.

    Parameters:
        source_dir (str): Path to the source directory containing the original Parquet files.
        destination_dir (str): Path to the destination directory for BIDS-compliant files.
    """
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Track session mapping for each subject
    session_mapping = defaultdict(dict)  # {subject: {uuid: session_number}}
    
    for file in os.listdir(source_dir):
        if file.startswith("P") and file.endswith(".parquet"):  # Check for expected file naming
            # Extract subject ID and session UUID
            sub_id = file.split("_")[0]
            session_uuid = file.split("_")[1].replace(".parquet", "")
            sub_bids = f"sub-{sub_id}"  # Convert to BIDS format
            
            # Assign session ID starting from 1 for each unique UUID
            if session_uuid not in session_mapping[sub_id]:
                session_mapping[sub_id][session_uuid] = len(session_mapping[sub_id]) + 1
            session_id = session_mapping[sub_id][session_uuid]
            ses_bids = f"ses-{session_id}"
            
            # Define paths
            sub_dir = os.path.join(destination_dir, sub_bids, ses_bids, "motion")
            os.makedirs(sub_dir, exist_ok=True)
            
            # Generate BIDS filename
            bids_filename = f"{sub_bids}_{ses_bids}_task-behavioralbiometrics_tracksys-VR_motion.tsv"
            bids_filepath = os.path.join(sub_dir, bids_filename)
            
            # Convert Parquet to TSV
            original_filepath = os.path.join(source_dir, file)
            try:
                # Read Parquet file and save as .tsv
                df = pd.read_parquet(original_filepath)
                df.to_csv(bids_filepath, sep="\t", index=False)
                print(f"Converted: {file} -> {bids_filepath}")
            except Exception as e:
                print(f"Failed to convert {file}: {e}")

# Example usage
source_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_orginal"
destination_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_converted"
convert_to_bids(source_directory, destination_directory)

