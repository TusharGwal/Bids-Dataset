\# XR Dataset BIDS Converter

This repository contains tools and scripts for converting XR datasets
into the \*\*BIDS motion data format\*\*.

\## Overview

The \*\*Brain Imaging Data Structure (BIDS)\*\* is a standardized format
for organizing and sharing datasets. This repository provides scripts
for transforming XR motion data into BIDS format, including generating
metadata and organizing files according to the BIDS specification.

\-\--

\## Conversion Steps

\### 1. Download the XR Dataset

Use the following script to download the XR dataset from Hugging Face.
The example below excludes the \`boxrr23\` directory:

\`\`\`python from huggingface_hub import snapshot_download

\# Download the dataset while excluding the boxrr23 directory local_dir
= snapshot_download( repo_id=\"cschell/xr-motion-dataset-catalogue\",
repo_type=\"dataset\", ignore_patterns=\[\"boxrr23/\*\*\"\],
local_dir=r\"C:\\Users\\tusha\\xr_motion_datasets\" )

print(f\"Dataset downloaded to: {local_dir}\") 2. Update Source and
Destination Directories Update the source_folder and destination_folder
in the relevant conversion script folder for the dataset you want to
process.

3.Once the directories are updated, Execute Shell Script

It runs the scripts in the following order to complete the conversion:

Conversion Script: Processes raw XR data and organizes it into the BIDS
motion format. Generate Metadata Script: Creates the necessary metadata
files (e.g., dataset_description.json, participants.tsv, json sidecar,
readme files). Generate Channels Script: Generates channel configuration
files, if required, for the dataset.
