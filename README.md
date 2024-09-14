# Wav2Lip with Dynamic Masking

## Introduction

This repository is a modified implementation of Wav2Lip, enhanced with **Dynamic Masking**. The main objective of this version is to dynamically detect the lips in a video frame, determine whether the lips are open or closed, and apply masking accordingly for more accurate and natural-looking lip synchronization.

**Wav2Lip** is a deep learning model designed for lip synchronization, ensuring that the lip movements in a video correspond to the given audio. Our extension focuses on adding dynamic masking to the model to improve results in more challenging scenarios, such as when lips are closed or partially open.

## Features

- **Dynamic Lip Detection:** The system first identifies the lips in each video frame.
- **Lip State Detection:** Determines whether the lips are open or closed.
- **Dynamic Masking:** Applies masking only when lips are open, improving the overall quality and realism of lip-syncing.
- **High-Quality Lip Syncing:** As in the original Wav2Lip, this model achieves state-of-the-art lip synchronization using deep learning techniques.

## Requirements

```bash
pip install -r requirements.txt
```

## Model Architecture

1. **Lip Detection Module:**  
   This module uses pre-trained models (such as dlib or OpenCV's facial landmark detection) to detect the region of interest (ROI) where the lips are located.

2. **Lip State Detection:**  
   A classifier that determines whether the lips are open or closed. The lip state influences the next step, which is the application of the mask.

3. **Dynamic Masking:**  
   The mask is applied only when lips are open, preventing the generation of unnecessary artifacts when the lips are closed. This mask is updated frame-by-frame to ensure that it follows the natural movement of the lips.

4. **Lip Sync Generator:**  
   This module takes both the dynamically masked lip regions and the audio signal to generate lip-synced movements. It is an extension of the original Wav2Lip model.

## Run

```bash
streamlit run app.py
```
