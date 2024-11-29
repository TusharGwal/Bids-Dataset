#!/bin/bash

if ! command -v python &> /dev/null
then
    echo "Python is not installed. Please install it and try again."
    exit 1
fi

python_files1=(
    "./1/liebers_beat_saber23/LBS23_Bids_convert.py"
    "./1/liebers_beat_saber23/generate_LBS23_metadata.py"
    "./generate_channels.py"
)

python_files2=(
    "./2/liebers_hand22/LH2-2Bids_convert.py"
    "./2/liebers_hand22/generate_LH22_metadata.py"
    "./generate_channels.py"
)

python_files3=(
    "./3/liebers_lab_study21/LLS21_bids_convert.py"
    "./3/liebers_lab_study21/generate_LLS21_metadata.py"
    "./generate_channels.py"
)

python_files4=(
    "./4/moore_cross_domain23/mcd_convert.py"
    "./4/moore_cross_domain23/generate_mcd_metadata.py"
    "./generate_channels.py"
)

python_files5=(
    "./5/vr_net/Vr_net_bids_convert.py"
    "./5/vr_net/generate_Vr_net_metadata.py"
    "./generate_channels.py"
)

python_files6=(
    "./6/who_is_alyx/wia_convert.py"
    "./6/who_is_alyx/generate_wia_metadata.py"
    "./generate_channels.py"
)

# Get user input
echo "Enter your choice:"
echo "  '1' - Run liebers_beat_saber23"
echo "  '2' - Run liebers_hand22"
echo "  '3' - Run liebers_lab_study21"
echo "  '4' - Run moore_cross_domain23"
echo "  '5' - Run vr_net"
echo "  '6' - Run who_is_alyx"
echo "  'none' - Skip running any files"
read -p "Enter your choice (1/2/3/4/5/6/none): " user_choice

python_files=($(find . -type f -name "*.py"))

# Process user input
if [ "$user_choice" == "1" ]; then
    echo "Running liebers_beat_saber23 Python files..."
    for file in "${python_files1[@]}"; do
        echo "Running $file..."
        python "$file"
        if [ $? -ne 0 ]; then
            echo "Error running $file. Exiting."
            exit 1
        fi
    done

elif [ "$user_choice" == "2" ]; then
    echo "Running liebers_hand22 Python files..."
    for file in "${python_files2[@]}"; do
        echo "Running $file..."
        python "$file"
        if [ $? -ne 0 ]; then
            echo "Error running $file. Exiting."
            exit 1
        fi
    done

elif [ "$user_choice" == "3" ]; then
    echo "Running liebers_lab_study21 Python files..."
    for file in "${python_files3[@]}"; do
        echo "Running $file..."
        python "$file"
        if [ $? -ne 0 ]; then
            echo "Error running $file. Exiting."
            exit 1
        fi
    done

elif [ "$user_choice" == "4" ]; then
    echo "Running moore_cross_domain23 Python files..."
    for file in "${python_files4[@]}"; do
        echo "Running $file..."
        python "$file"
        if [ $? -ne 0 ]; then
            echo "Error running $file. Exiting."
            exit 1
        fi
    done

elif [ "$user_choice" == "5" ]; then
    echo "Running vr_net Python files..."
    for file in "${python_files5[@]}"; do
        echo "Running $file..."
        python "$file"
        if [ $? -ne 0 ]; then
            echo "Error running $file. Exiting."
            exit 1
        fi
    done

elif [ "$user_choice" == "6" ]; then
    echo "Running who_is_alyx Python files..."
    for file in "${python_files6[@]}"; do
        echo "Running $file..."
        python "$file"
        if [ $? -ne 0 ]; then
            echo "Error running $file. Exiting."
            exit 1
        fi
    done

elif [ "$user_choice" == "none" ]; then
    echo "No files will be run."
    exit 0

else
    echo "Invalid choice. Exiting."
    exit 1
fi

echo "Script execution completed!"
