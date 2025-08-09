# Bottle Defect Detection with YOLOv8

This repository contains the full source code and trained model for a real-time computer vision project to detect defects on bottle caps. The project is built using the Ultralytics YOLOv8n model, trained on a custom dataset to identify "open cap" and "good cap" states.

## Project Description

The goal of this project is to implement an automated quality control system for a manufacturing line by using a camera to inspect bottle caps. The trained model can perform live inference to classify a bottle cap as either `open cap` or `good cap` with high accuracy. This allows for immediate identification of production defects, preventing faulty products from reaching the consumer.

### Key Features
- **Real-time Inference:** Capable of processing live video streams from a webcam.
- **Custom Dataset:** Trained on a proprietary dataset of 300 images with two distinct classes.
- **High Accuracy:** The trained model achieved a robust mAP50-95 score of **0.831** on the validation set.

## Dataset

The model was trained on a custom dataset containing 300 images, meticulously labeled into the following two classes:

- **`open cap`**: 150 images
- **`good cap`**: 150 images

The dataset was split into training, validation, and testing sets, with the distribution configured in the `data.yaml` file.

## Model and Training

The model of choice for this project is **YOLOv8n** (YOLOv8 Nano), which offers a great balance between performance and speed, making it ideal for real-time applications.

### Training Configuration

The training was performed on a local GPU with the following configuration:
- **Model:** `yolov8n.pt`
- **Epochs:** 50
- **Image Size:** 640x640 pixels
- **Early Stopping:** `patience=10` to prevent overfitting.
- **Device:** GPU (CUDA)

The trained model weights are located in the `runs/detect/train/weights/` folder, with the final best weights named `best.pt`.

## Getting Started

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- An NVIDIA GPU with CUDA support
- Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Srevarshan05/Bottle-defect-CV.git](https://github.com/Srevarshan05/Bottle-defect-CV.git)
    cd Bottle-defect-CV
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv gpu
    .\gpu\Scripts\activate
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Live Inference

To run the model in real-time on your webcam, use the `live_inference_fix.py` script. This script automatically configures the webcam to match the training resolution for optimal performance.

1.  **Ensure your webcam is not being used by other applications.**
2.  **Run the inference script:**
    ```bash
    python live_inference_fix.py
    ```

A new window will open displaying the live feed from your webcam with real-time object detections. Press the `q` key to exit the program.

## Inference on Video Files

To test the model on a pre-recorded video, use the `video_inference.py` script.

1.  **Update the `source` variable** in the script to point to your video file's path.
2.  **Run the script:**
    ```bash
    python video_inference.py
    ```

The processed video with detections will be saved to the `runs/detect/` folder.