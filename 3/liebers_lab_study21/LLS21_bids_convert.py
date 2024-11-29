import os
import re
import pandas as pd
from pathlib import Path

# Define the folder containing the files
source_folder = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_lab_study21"
destination_folder = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_lab_study21_converted"

# Create a regular expression pattern to match the new file naming structure
pattern = re.compile(r'(.+?)_p(\d+)_([^_]+)_session(\d+)_repetition(\d+)')

def organize_files():
    # Iterate over all files in the source folder
    for filename in os.listdir(source_folder):
        # Process only .parquet files
        if filename.endswith(".parquet"):
            match = pattern.match(filename)
            if match:
                task, pid, tracksys, session, rep = match.groups()

                # Convert data into required format
                pid_str = f"p{pid}"
                task = task.lower()
                tracksys = f"tracksys-{tracksys.lower()}"
                session_str = f"{session}"
                run_str = f"run-{int(rep):02d}"

                # Construct the new filename
                new_filename = f"sub-{pid_str}_ses-{session_str}_task-{task}_{tracksys}_{run_str}_motion.tsv"

                # Create the necessary directories
                pid_dir = Path(destination_folder) / f"sub-{pid_str}"
                session_dir = pid_dir / f"ses-{session_str}" / "motion"
                session_dir.mkdir(parents=True, exist_ok=True)

                # Convert .parquet to .tsv and save in the new directory
                source_path = Path(source_folder) / filename
                destination_path = session_dir / new_filename

                # Read parquet file and save it as .tsv
                df = pd.read_parquet(source_path)
                df.to_csv(destination_path, sep='\t', index=False)

                print(f"Converted and copied: {filename} -> {destination_path}")

if __name__ == "__main__":
    organize_files()