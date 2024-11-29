# import os
# import pandas as pd
# import json

# def generate_channels_metadata(tsv_file):
#     """
#     Generate channels.tsv and channels.json metadata for a given motion TSV file.

#     Parameters:
#         tsv_file (str): Path to the motion TSV file.
#     """
#     # Define metadata for each channel
#     channels_metadata = [
#         {"name": "delta_time_ms", "type": "Time", "units": "ms"},
#         {"name": "head_pos_x", "type": "Position", "units": "cm"},
#         {"name": "head_pos_y", "type": "Position", "units": "cm"},
#         {"name": "head_pos_z", "type": "Position", "units": "cm"},
#         {"name": "head_rot_w", "type": "Rotation", "units": "unitless"},
#         {"name": "head_rot_x", "type": "Rotation", "units": "unitless"},
#         {"name": "head_rot_y", "type": "Rotation", "units": "unitless"},
#         {"name": "head_rot_z", "type": "Rotation", "units": "unitless"},
#         {"name": "left_hand_pos_x", "type": "Position", "units": "cm"},
#         {"name": "left_hand_pos_y", "type": "Position", "units": "cm"},
#         {"name": "left_hand_pos_z", "type": "Position", "units": "cm"},
#         {"name": "left_hand_rot_w", "type": "Rotation", "units": "unitless"},
#         {"name": "left_hand_rot_x", "type": "Rotation", "units": "unitless"},
#         {"name": "left_hand_rot_y", "type": "Rotation", "units": "unitless"},
#         {"name": "left_hand_rot_z", "type": "Rotation", "units": "unitless"},
#         {"name": "right_hand_pos_x", "type": "Position", "units": "cm"},
#         {"name": "right_hand_pos_y", "type": "Position", "units": "cm"},
#         {"name": "right_hand_pos_z", "type": "Position", "units": "cm"},
#         {"name": "right_hand_rot_w", "type": "Rotation", "units": "unitless"},
#         {"name": "right_hand_rot_x", "type": "Rotation", "units": "unitless"},
#         {"name": "right_hand_rot_y", "type": "Rotation", "units": "unitless"},
#         {"name": "right_hand_rot_z", "type": "Rotation", "units": "unitless"},
#         {"name": "user", "type": "Metadata", "units": "unitless"},
#         {"name": "session", "type": "Metadata", "units": "unitless"},
#     ]
    
#     # Create a DataFrame for channels.tsv
#     channels_df = pd.DataFrame(channels_metadata)
    
#     # Define output paths
#     channels_tsv_path = tsv_file.replace("_motion.tsv", "_channels.tsv")
#     channels_json_path = tsv_file.replace("_motion.tsv", "_channels.json")
    
#     # Save channels.tsv
#     channels_df.to_csv(channels_tsv_path, sep="\t", index=False)
#     print(f"Generated channels.tsv: {channels_tsv_path}")
    
#     # Save channels.json (additional metadata)
#     channels_json_content = {
#         "delta_time_ms": "Time in milliseconds between consecutive samples.",
#         "head_pos_x": "Head position along the X-axis.",
#         "head_pos_y": "Head position along the Y-axis.",
#         "head_pos_z": "Head position along the Z-axis.",
#         "head_rot_w": "Head rotation quaternion component W.",
#         "head_rot_x": "Head rotation quaternion component X.",
#         "head_rot_y": "Head rotation quaternion component Y.",
#         "head_rot_z": "Head rotation quaternion component Z.",
#         "left_hand_pos_x": "Left hand position along the X-axis.",
#         "left_hand_pos_y": "Left hand position along the Y-axis.",
#         "left_hand_pos_z": "Left hand position along the Z-axis.",
#         "left_hand_rot_w": "Left hand rotation quaternion component W.",
#         "left_hand_rot_x": "Left hand rotation quaternion component X.",
#         "left_hand_rot_y": "Left hand rotation quaternion component Y.",
#         "left_hand_rot_z": "Left hand rotation quaternion component Z.",
#         "right_hand_pos_x": "Right hand position along the X-axis.",
#         "right_hand_pos_y": "Right hand position along the Y-axis.",
#         "right_hand_pos_z": "Right hand position along the Z-axis.",
#         "right_hand_rot_w": "Right hand rotation quaternion component W.",
#         "right_hand_rot_x": "Right hand rotation quaternion component X.",
#         "right_hand_rot_y": "Right hand rotation quaternion component Y.",
#         "right_hand_rot_z": "Right hand rotation quaternion component Z.",
#         "user": "Unique user identifier.",
#         "session": "Unique session identifier.",
#     }
#     with open(channels_json_path, "w") as f:
#         json.dump(channels_json_content, f, indent=4)
#     print(f"Generated channels.json: {channels_json_path}")

# def process_files(data_dir):
#     """
#     Process all motion TSV files in the directory to generate channels.tsv and channels.json.
    
#     Parameters:
#         data_dir (str): Directory containing motion TSV files.
#     """
#     for root, _, files in os.walk(data_dir):
#         for file in files:
#             if file.endswith("_motion.tsv"):
#                 tsv_file = os.path.join(root, file)
#                 try:
#                     generate_channels_metadata(tsv_file)
#                 except Exception as e:
#                     print(f"Failed to process {file}: {e}")

# # Example usage
# data_directory = r"d:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_converted"  # Replace with the path to your dataset
# process_files(data_directory)

# import os
# import pandas as pd
# import json

# def generate_channels_metadata(tsv_file):
#     """
#     Generate channels.tsv and channels.json metadata for a given motion TSV file.

#     Parameters:
#         tsv_file (str): Path to the motion TSV file.
#     """
#     # Define metadata for each channel
#     channels_metadata = [
#         {"name": "delta_time_ms", "component": "n/a", "type": "LATENCY", "tracked_point": "system", "units": "ms"},
#         {"name": "head_pos_x", "component": "x", "type": "POS", "tracked_point": "head", "units": "cm"},
#         {"name": "head_pos_y", "component": "y", "type": "POS", "tracked_point": "head", "units": "cm"},
#         {"name": "head_pos_z", "component": "z", "type": "POS", "tracked_point": "head", "units": "cm"},
#         {"name": "head_rot_w", "component": "quat_w", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
#         {"name": "head_rot_x", "component": "quat_x", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
#         {"name": "head_rot_y", "component": "quat_y", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
#         {"name": "head_rot_z", "component": "quat_z", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
#         {"name": "left_hand_pos_x", "component": "x", "type": "POS", "tracked_point": "left_hand", "units": "cm"},
#         {"name": "left_hand_pos_y", "component": "y", "type": "POS", "tracked_point": "left_hand", "units": "cm"},
#         {"name": "left_hand_pos_z", "component": "z", "type": "POS", "tracked_point": "left_hand", "units": "cm"},
#         {"name": "left_hand_rot_w", "component": "quat_w", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
#         {"name": "left_hand_rot_x", "component": "quat_x", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
#         {"name": "left_hand_rot_y", "component": "quat_y", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
#         {"name": "left_hand_rot_z", "component": "quat_z", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
#         {"name": "right_hand_pos_x", "component": "x", "type": "POS", "tracked_point": "right_hand", "units": "cm"},
#         {"name": "right_hand_pos_y", "component": "y", "type": "POS", "tracked_point": "right_hand", "units": "cm"},
#         {"name": "right_hand_pos_z", "component": "z", "type": "POS", "tracked_point": "right_hand", "units": "cm"},
#         {"name": "right_hand_rot_w", "component": "quat_w", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
#         {"name": "right_hand_rot_x", "component": "quat_x", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
#         {"name": "right_hand_rot_y", "component": "quat_y", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
#         {"name": "right_hand_rot_z", "component": "quat_z", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
#     ]

    
#     # Create a DataFrame for channels.tsv
#     channels_df = pd.DataFrame(channels_metadata)
    
#     # Define output paths
#     channels_tsv_path = tsv_file.replace("_motion.tsv", "_channels.tsv")
#     channels_json_path = tsv_file.replace("_motion.tsv", "_channels.json")
    
#     # Save channels.tsv
#     channels_df.to_csv(channels_tsv_path, sep="\t", index=False)
#     print(f"Generated channels.tsv: {channels_tsv_path}")
    
#     # Save channels.json (additional metadata)
#     channels_json_content = {
#         "reference_frame": {
#             "Levels": {
#                 "global": {
#                     "SpatialAxes": "ALS",
#                     "RotationOrder": "ZXY",
#                     "RotationRule": "right-hand"
#                 }
#             }
#         }
#     }
#     with open(channels_json_path, "w") as f:
#         json.dump(channels_json_content, f, indent=4)
#     print(f"Generated channels.json: {channels_json_path}")

# def process_files(data_dir):
#     """
#     Process all motion TSV files in the directory to generate channels.tsv and channels.json.
    
#     Parameters:
#         data_dir (str): Directory containing motion TSV files.
#     """
#     for root, _, files in os.walk(data_dir):
#         for file in files:
#             if file.endswith("_motion.tsv"):
#                 tsv_file = os.path.join(root, file)
#                 try:
#                     generate_channels_metadata(tsv_file)
#                 except Exception as e:
#                     print(f"Failed to process {file}: {e}")

# # Example usage
# data_directory = r"d:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_converted"  # Replace with the path to your dataset
# process_files(data_directory)

import os
import pandas as pd
import json

def generate_channels_metadata(tsv_file):
    """
    Generate channels.tsv and channels.json metadata for a given motion TSV file.

    Parameters:
        tsv_file (str): Path to the motion TSV file.
    """
    # Define metadata for each channel
    channels_metadata = [
        {"name": "delta_time_ms", "component": "n/a", "type": "LATENCY", "tracked_point": "system", "units": "ms"},
        {"name": "head_pos_x", "component": "x", "type": "POS", "tracked_point": "head", "units": "cm"},
        {"name": "head_pos_y", "component": "y", "type": "POS", "tracked_point": "head", "units": "cm"},
        {"name": "head_pos_z", "component": "z", "type": "POS", "tracked_point": "head", "units": "cm"},
        {"name": "head_rot_w", "component": "quat_w", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
        {"name": "head_rot_x", "component": "quat_x", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
        {"name": "head_rot_y", "component": "quat_y", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
        {"name": "head_rot_z", "component": "quat_z", "type": "ORNT", "tracked_point": "head", "units": "n/a"},
        {"name": "left_hand_pos_x", "component": "x", "type": "POS", "tracked_point": "left_hand", "units": "cm"},
        {"name": "left_hand_pos_y", "component": "y", "type": "POS", "tracked_point": "left_hand", "units": "cm"},
        {"name": "left_hand_pos_z", "component": "z", "type": "POS", "tracked_point": "left_hand", "units": "cm"},
        {"name": "left_hand_rot_w", "component": "quat_w", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
        {"name": "left_hand_rot_x", "component": "quat_x", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
        {"name": "left_hand_rot_y", "component": "quat_y", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
        {"name": "left_hand_rot_z", "component": "quat_z", "type": "ORNT", "tracked_point": "left_hand", "units": "n/a"},
        {"name": "right_hand_pos_x", "component": "x", "type": "POS", "tracked_point": "right_hand", "units": "cm"},
        {"name": "right_hand_pos_y", "component": "y", "type": "POS", "tracked_point": "right_hand", "units": "cm"},
        {"name": "right_hand_pos_z", "component": "z", "type": "POS", "tracked_point": "right_hand", "units": "cm"},
        {"name": "right_hand_rot_w", "component": "quat_w", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
        {"name": "right_hand_rot_x", "component": "quat_x", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
        {"name": "right_hand_rot_y", "component": "quat_y", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
        {"name": "right_hand_rot_z", "component": "quat_z", "type": "ORNT", "tracked_point": "right_hand", "units": "n/a"},
    ]

    # Create a DataFrame for channels.tsv
    channels_df = pd.DataFrame(channels_metadata)
    
    # Define output paths
    channels_tsv_path = tsv_file.replace("_motion.tsv", "_channels.tsv")
    channels_json_path = tsv_file.replace("_motion.tsv", "_channels.json")
    
    # Save channels.tsv
    channels_df.to_csv(channels_tsv_path, sep="\t", index=False)
    print(f"Generated channels.tsv: {channels_tsv_path}")
    
    # Save channels.json with updated metadata
    channels_json_content = {
        "reference_frame": {
            "Levels": {
                "global": {
                    "SpatialAxes": "RAS",
                    "RotationOrder": "WXYZ",
                    "RotationRule": "right-hand",
                    "Description": "Global coordinate system with Right-Anterior-Superior orientation"
                }
            }
        },
        "tracked_point": {
            "Description": "The body part or object being tracked",
            "Levels": {
                "head": "Participant's head",
                "left_hand": "Participant's left hand",
                "right_hand": "Participant's right hand"
            }
        },
        "component": {
            "Description": "Spatial component or quaternion component for orientation",
            "Levels": {
                "x": "X-axis",
                "y": "Y-axis",
                "z": "Z-axis",
                "quat_w": "Quaternion scalar component",
                "quat_x": "Quaternion x component",
                "quat_y": "Quaternion y component",
                "quat_z": "Quaternion z component"
            }
        },
        "type": {
            "Description": "Type of measurement",
            "Levels": {
                "LATENCY": "Time measurement",
                "POS": "Position",
                "ORNT": "Orientation"
            }
        },
        "units": {
            "Description": "Units of measurement",
            "Levels": {
                "ms": "Milliseconds",
                "cm": "Centimeters",
                "n/a": "Not applicable (for quaternions)"
            }
        }
    }
    with open(channels_json_path, "w") as f:
        json.dump(channels_json_content, f, indent=4)
    print(f"Generated channels.json: {channels_json_path}")

def process_files(data_dir):
    """
    Process all motion TSV files in the directory to generate channels.tsv and channels.json.
    
    Parameters:
        data_dir (str): Directory containing motion TSV files.
    """
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith("_motion.tsv"):
                tsv_file = os.path.join(root, file)
                try:
                    generate_channels_metadata(tsv_file)
                except Exception as e:
                    print(f"Failed to process {file}: {e}")

# Example usage
data_directory = r"d:\Motion Data Project\Milestone 2\xr_motion_datasets\liebers_beat_saber23\liebers_beat_saber23_converted" # Replace with the path to your dataset
process_files(data_directory)

