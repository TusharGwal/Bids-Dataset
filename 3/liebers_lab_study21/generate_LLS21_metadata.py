import os
import pandas as pd
import numpy as np
import json

def analyze_motion_data(tsv_file):
    """
    Analyze motion data from a TSV file to calculate sampling frequency and other parameters.

    Parameters:
        tsv_file (str): Path to the TSV file.
    
    Returns:
        dict: A dictionary of calculated parameters.
    """
    # Load the TSV file
    df = pd.read_csv(tsv_file, sep='\t')
    
    # Calculate sampling frequency (Hz)
    delta_times = df['delta_time_ms'].dropna()
    if len(delta_times) > 1:
        mean_delta_time_ms = np.mean(delta_times)
        sampling_frequency = 1000 / mean_delta_time_ms  # Convert ms to Hz
    else:
        sampling_frequency = None

    # Determine the number of tracked points
    tracked_points_count = len([
        col for col in df.columns 
        if 'pos' in col or 'rot' in col
    ]) // 3  # Divide by 3 for x, y, z or w, x, y, z components

    # Extract unique user and session information
    unique_users = df['user'].nunique()
    unique_sessions = df['session'].nunique()
    scenes = df['scene'].iloc[1]
    # Generate metadata
    metadata = {
        "SamplingFrequency": sampling_frequency,
        "TrackedPointsCount": tracked_points_count,
        "UniqueUsers": unique_users,
        "UniqueSessions": unique_sessions,
        "UniqueScenes": scenes
    }
    
    return metadata

def create_motion_sidecar(tsv_file, metadata):
    """
    Create a JSON sidecar for a given motion TSV file based on calculated metadata.

    Parameters:
        tsv_file (str): Path to the TSV file.
        metadata (dict): Calculated metadata for the motion file.
    """
    sidecar_content = {
        "TaskName": metadata.get("UniqueScenes"),
        "SamplingFrequency": metadata.get("SamplingFrequency"),
        "CoordinateSystem": "X (Right), Y (Up), Z (Forward)",
        "RotationRepresentation": "Quaternions",
        "Units": "Centimeters",
        "TimeEncoding": "Milliseconds",
        "TrackedPointsCount": metadata.get("TrackedPointsCount"),
        "InstitutionName": "Your Institution",
        "InstitutionAddress": "Address, City, Country",
        "TaskDescription": "User movements captured during behavioral biometric tasks.",
        "SoftwareVersions": "1.0"
    }
    
    json_path = tsv_file.replace("_motion.tsv", "_motion.json")
    with open(json_path, "w") as f:
        json.dump(sidecar_content, f, indent=4)
    print(f"Generated JSON sidecar: {json_path}")

def process_motion_files(data_dir):
    """
    Process all motion TSV files in the directory to compute metadata and create JSON sidecars.

    Parameters:
        data_dir (str): Directory containing motion TSV files.
    """
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith("_motion.tsv"):
                tsv_file = os.path.join(root, file)
                try:
                    # Analyze motion data
                    metadata = analyze_motion_data(tsv_file)
                    
                    # Generate JSON sidecar
                    create_motion_sidecar(tsv_file, metadata)
                except Exception as e:
                    print(f"Failed to process {file}: {e}")

def create_dataset_description(output_dir):
    """
    Creates the dataset_description.json file.
    
    Parameters:
        output_dir (str): Path to the output directory.
    """
    dataset_description = {
        "Name": "XR Motion Dataset",
        "BIDSVersion": "1.8.0",
        "DatasetType": "raw",
        "Authors": ["Kinematic Research Team"],
        "Acknowledgements": "Acknowledgements for dataset collection.",
        "Funding": ["Grant XYZ or Funding Agency"],
        "License": "CC BY 4.0",
        "DatasetDescription": "A standardized catalogue of XR motion datasets aligned with consistent kinematic research standards.",
    }
    
    # Write dataset_description.json
    output_path = os.path.join(output_dir, "dataset_description.json")
    with open(output_path, "w") as f:
        json.dump(dataset_description, f, indent=4)
    print(f"Generated dataset_description.json: {output_path}")

readme_content = """# XR Motion Dataset

## Overview

his dataset is part of the **XR Motion Dataset Catalogue**, designed to support research on behavioral biometrics in Virtual Reality (VR). It was collected as part of the study *"Understanding User Identification in Virtual Reality Through Behavioral Biometrics and the Effect of Body Normalization"* by Liebers et al. The study explores how unique motion patterns can identify users and how normalizing body proportions impacts this identification.

## Authors

- **Jonathan Liebers**  
- **Mark Abdelaziz**  
- **Lukas Mecke**  
- **Alia Saad**  
- **Jonas Auda**  
- **Uwe Gruenefeld**  
- **Florian Alt**  
- **Stefan Schneegass**  

## License

This dataset is made available under the Creative Commons CC0 license. Information on CC0 can be found here: https://creativecommons.org/share-your-work/public-domain/cc0/

## Format

The dataset is formatted according to the Brain Imaging Data Structure (BIDS) specification, with a focus on motion data. See the dataset_description.json file for the specific version used.

Generally, you can find data in the .tsv files and descriptions in the accompanying .json files.

An important BIDS definition to consider is the "Inheritance Principle", which is described in the BIDS specification under the following link:

https://bids-specification.rtfd.io/en/stable/02-common-principles.html#the-inheritance-principle

## Details about the experiment

## Details about the Experiment

The study investigates behavioral biometrics in VR, focusing on:
1. Identifying users through body movements.  
2. Evaluating the impact of body normalization on identification accuracy.

### Data Collection

- **Tracked Points**: Head, Left Hand, Right Hand
- **Measurements**: 
  - Position (x, y, z) in centimeters
  - Orientation (quaternion: w, x, y, z)
  - System latency in milliseconds

### Coordinate System

- X: Right
- Y: Up
- Z: Forward

## Usage

To use this dataset with the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("cschell/xr-motion-dataset-catalogue", "liebers_lab_study21", trust_remote_code=True)
```


## Citation

If you use this dataset in your research, please cite the original paper:

```
@inproceedings{liebers2021understanding,
  title={Understanding User Identification in Virtual Reality Through Behavioral Biometrics and the Effect of Body Normalization},
  author={Liebers, Jonathan and Abdelaziz, Mark and Mecke, Lukas and Saad, Alia and Auda, Jonas and Gruenefeld, Uwe and Alt, Florian and Schneegass, Stefan},
  booktitle={Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems},
  year={2021},
  organization={ACM},
  doi={10.1145/3411764.3445528}
}
```

For more information about the dataset and its collection, please refer to the original paper.
"""

def create_readme(directory, content):
    filepath = os.path.join(directory, "README.md")
    with open(filepath, "w") as f:
        f.write(content)


# Example usage
data_directory = r"D:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_lab_study21\liebers_lab_study21_converted" # Replace with the path to your dataset
create_dataset_description(data_directory)
process_motion_files(data_directory)
create_readme(data_directory, readme_content)
