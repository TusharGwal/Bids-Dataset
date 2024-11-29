import os
import re
import pandas as pd
from pathlib import Path
from shutil import copy2

# Define the folder containing the files
source_folder = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_hand22\liebers_hand22_orginial"
destination_folder = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_hand22\Liebers_hand22_converted"

# Create a regular expression pattern to match the file naming structure
pattern = re.compile(r'SCENE-(\w+)_XR-(\w+)_PID-(\d+)_REP-(\d+)_SESSION-(\d+)')

def organize_files():
    # Count original files
    original_count = len([f for f in os.listdir(source_folder) if f.endswith(".parquet")])
    converted_count = 0  # Initialize converted count

    # Iterate over all files in the source folder
    for filename in os.listdir(source_folder):
        # Process only .parquet files
        if filename.endswith(".parquet"):
            match = pattern.match(filename)
            if match:
                scene, tracksys, pid, rep, session = match.groups()

                # Convert data into required format
                pid_str = f"PID{pid}"
                task = scene.lower()
                tracksys = f"tracksys-{tracksys.lower()}"
                session_str = f"ses-{session}"
                run_str = f"run-{int(rep):02d}"

                # Construct the new filename, including session
                new_filename = f"sub-{pid_str}_ses-{session}_task-{task}_{tracksys}_{run_str}_motion.tsv"

                # Create the necessary directories
                pid_dir = Path(destination_folder) / f"sub-{pid_str}"
                session_dir = pid_dir / session_str / "motion"
                session_dir.mkdir(parents=True, exist_ok=True)

                # Convert .parquet to .tsv and save in the new directory
                source_path = Path(source_folder) / filename
                destination_path = session_dir / new_filename

                # Read parquet file and save it as .tsv
                df = pd.read_parquet(source_path)
                df.to_csv(destination_path, sep='\t', index=False)

                converted_count += 1 # Increment converted count
                print(f"Converted and copied: {filename} -> {destination_path}")

    print(f"Original files: {original_count}")
    print(f"Converted files: {converted_count}")
    if original_count == converted_count:
        print("File counts match!")
    else:
        print("File counts do not match!")


if __name__ == "__main__":
    organize_files()
