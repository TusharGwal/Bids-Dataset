import os
import re
import pandas as pd

def convert_and_copy_files(src_dir, dest_dir):
    # Regex pattern for extracting details from file names
    file_pattern = r'FAB(?P<player_id>\d+)(?P<gender>[MF])_Build(?P<session>[ABab])\.parquet'
    total_files = sum(1 for _, _, files in os.walk(src_dir) for file in files if file.endswith('.parquet'))
    file_count = 0
    for root, _, files in os.walk(src_dir):
        for file_name in files:
            match = re.match(file_pattern, file_name)
            if match and file_name.endswith('.parquet'):
                player_id = match.group('player_id')
                gender = match.group('gender')
                session = match.group('session').upper()  # Normalize to uppercase

                # Define the BIDS-compliant file name and directory structure
                sub_folder = f"sub-FAB{player_id}{gender}"
                ses_folder = f"ses-{session}"
                bids_file_name = f"sub-FAB{player_id}{gender}_ses-{session}_task-assembly_tracksys-xr_motion.tsv"

                # Create the BIDS folder structure in the destination directory
                dest_sub_dir = os.path.join(dest_dir, sub_folder, ses_folder, 'motion')
                os.makedirs(dest_sub_dir, exist_ok=True)

                # Convert parquet to TSV and save in the BIDS-compliant structure
                src_file_path = os.path.join(root, file_name)
                dest_file_path = os.path.join(dest_sub_dir, bids_file_name)

                # Read parquet, convert to TSV
                df = pd.read_parquet(src_file_path)
                df.to_csv(dest_file_path, sep='\t', index=False)
                print(f"Converted and saved: {dest_file_path}")
                file_count += 1

    print(f"Total files converted: {file_count}")
    print(f"Total files in source directory: {total_files}")
    if file_count == total_files:
        print("Verification successful: All parquet files converted.")
    else:
        print(f"Verification failed: {total_files - file_count} files not converted.")


# Example usage
source_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\moore_cross_domain23\moore_cross_domain23_original"
destination_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\moore_cross_domain23\moore_cross_domain23_converted"
convert_and_copy_files(source_directory, destination_directory)
