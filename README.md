# Helmet Detection

## Overview

A custom object detection system using **YOLOv5** to identify whether individuals in images are wearing helmets. The model is trained on a custom dataset and integrated into a **Streamlit** web application, allowing real-time helmet detection for uploaded images.

---

## Features

- **YOLOv5 Object Detection**: Detects whether individuals in images are wearing helmets or not.
- **Streamlit Integration**: Simple, easy-to-use interface for real-time helmet detection in uploaded images.
- **Custom Dataset**: The model is trained on a custom dataset of helmet images.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Git
- Streamlit
- YOLOv5 repository

### Clone the Repository

```
git clone https://github.com/kavya-prabahar/Helmet-Detection.git
cd Helmet-Detection
```

Training the Model
Prepare the Dataset: Ensure you have a dataset with helmet and non-helmet images.
Train YOLOv5:

```
python train.py --img 640 --batch 16 --epochs 50 --data custom_dataset.yaml --weights yolov5s.pt --cache
Replace custom_dataset.yaml with your dataset configuration file.
```

Running the Web Application
After training, you can start the Streamlit web application:

```
streamlit run app.py
Upload an image and the model will detect whether the person is wearing a helmet or not.
```
