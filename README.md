Here's the formatted README.md file:

# XR Dataset BIDS Converter

This repository contains tools and scripts for converting XR datasets into the **BIDS motion data format**.

## Overview

The **Brain Imaging Data Structure (BIDS)** is a standardized format for organizing and sharing datasets. This repository provides scripts for transforming XR motion data into BIDS format, including generating metadata and organizing files according to the BIDS specification.

## Conversion Steps

### 1. Download the XR Dataset

Use the following script to download the XR dataset from Hugging Face. The example below excludes the `boxrr23` directory:

```python
from huggingface_hub import snapshot_download

# Download the dataset while excluding the boxrr23 directory
local_dir = snapshot_download(
    repo_id="cschell/xr-motion-dataset-catalogue",
    repo_type="dataset",
    ignore_patterns=["boxrr23/**"],
    local_dir=r"C:\Users\tusha\xr_motion_datasets"
)

print(f"Dataset downloaded to: {local_dir}")
```

### 2. Update Source and Destination Directories

Update the `source_folder` and `destination_folder` in the relevant conversion script folder for the dataset you want to process.

### 3. Execute Shell Script

Once the directories are updated, execute the shell script using the following commands:

```bash
chmod +x newDataScript.sh
./newDataScript.sh
```

The script will:
- Ask which dataset you want to convert
- Execute the corresponding codes to convert the XR-Motion Dataset into BIDS spec format
- Generate metadata and channels files

It runs the scripts in the following order to complete the conversion:

1. **Conversion Script**: Processes raw XR data and organizes it into the BIDS motion format.
2. **Generate Metadata Script**: Creates the necessary metadata files (e.g., dataset_description.json, participants.tsv, json sidecar, readme files).
3. **Generate Channels Script**: Generates channel configuration files, if required, for the dataset.

### 4. Verify the Dataset

After conversion, you can verify the dataset on the BIDS validator website: https://bids-standard.github.io/bids-validator/

For verification, a file count check is included, which compares the number of files in the source directory to the number of files converted into motion data.
