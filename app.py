import streamlit as st
import torch
from PIL import Image
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Raja/Desktop/Yolov5/yolov5/runs/train/exp2/weights/best.pt')

st.title("Helmet Detection")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    img = np.array(image)

    results = model(img)

    results.render()  

    result_image = Image.fromarray(results.ims[0])

    st.image(result_image, caption="Processed Image with Detections", use_column_width=True)

    st.write("Detection Results:")
    st.dataframe(results.pandas().xywh[0])  
