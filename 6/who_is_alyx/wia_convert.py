import os
import shutil
import pandas as pd
from datetime import datetime

# Define source and destination directories
source_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\who_is_alyx\who_is_alyx_original"  # Change this to the root of your existing data folder
destination_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\who_is_alyx\who_is_alyx_converted"  # Change this to the root of the new BIDS-compliant structure

# BIDS-compliant naming details
task_name = "behavioralbiometrics"
tracksys_name = "xr"

# Loop through each player directory
for player_folder in os.listdir(source_directory):
    player_path = os.path.join(source_directory, player_folder)
    
    # Only proceed if it's a directory and follows "PlayerNumber" format
    if os.path.isdir(player_path):
        # Extract player number (Assuming folder is named as "PlayerX")
        player_number = player_folder.replace("player_", "")  # Remove "Player" prefix to get the number
        
        # Loop through each date file in player directory
        for file_name in os.listdir(player_path):
            if file_name.endswith(".parquet"):
                # Extract the date from file name
                date_str = file_name.replace(".parquet", "")
                
                try:
                    # Convert date to "YYYYMMDD" format for BIDS compliance
                    date_formatted = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y%m%d")
                    
                    # Define BIDS-compliant session and file names
                    session_name = f"ses-{date_formatted}"
                    new_file_name = f"sub-{player_number}_ses-{date_formatted}_task-{task_name}_tracksys-{tracksys_name}_motion.tsv"
                    
                    # Define the destination paths
                    session_path = os.path.join(destination_directory, f"sub-{player_number}", session_name, "motion")
                    os.makedirs(session_path, exist_ok=True)
                    
                    # Read the parquet file and convert to TSV
                    source_file_path = os.path.join(player_path, file_name)
                    df = pd.read_parquet(source_file_path)
                    destination_file_path = os.path.join(session_path, new_file_name)
                    df.to_csv(destination_file_path, sep='\t', index=False)
                    
                    print(f"Converted and moved: {source_file_path} -> {destination_file_path}")
                
                except ValueError:
                    print(f"Skipping {file_name}: Date format not recognized.")

print("File conversion and reorganization complete.")