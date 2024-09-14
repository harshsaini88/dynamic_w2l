# Enhancement of Easywav2Lip through Dynamic Masking Approach

## Overview
This project enhances the Easywav2Lip model by implementing a dynamic masking approach. It aims to improve the lip synchronization quality in videos using the latest model checkpoints and additional tools.

## Installation and Setup

### Install gdown:
To download necessary files from Google Drive, install the `gdown` package:

```bash
pip install gdown
```

### Download Required Folders:

#### Checkpoints Folder:
Download the checkpoints folder using the following command:

```bash
gdown --folder https://drive.google.com/drive/folders/1ntfGv_H5zgYNu2DJLw7DlrJTJmhP3Rrl?usp=sharing
```

#### GFPGAN Folder:
Download the GFPGAN folder using this command:

```bash
gdown --folder https://drive.google.com/drive/folders/1kEfV7HPG2NfMPuHPv41PxKJtHTcSeFie?usp=sharing
```

### Install Necessary Requirements:

Ensure that **CUDA Version 11.8** is installed and properly configured on your system.

### Create Conda Environment:
Create a Conda environment specifically for this project:

```bash
conda create -n easywav2lip python==3.10
```

### Activate Conda Environment:
Activate the newly created environment:

```bash
conda activate easywav2lip
```

### Install Python Packages:
Install the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

To run the model and apply the dynamic masking approach, use the following command:

```bash
python run.py -video_file "video_path" -vocal_file "audio_path"
```

- Replace `"video_path"` with the path to your input video file.
- Replace `"audio_path"` with the path to your vocal (audio) file.

## Notes

- Ensure that the specified CUDA version (11.8) is installed and properly configured on your system.
- Make sure you have the necessary permissions to download the folders from Google Drive.
- Verify that all dependencies in `requirements.txt` are correctly installed.
