# -*- coding: utf-8 -*-
"""Inference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gesk60LDHw3pwU4-jlK5wIURtqbDFiaV
"""

import argparse
import cv2
import numpy as np
from tensorflow.keras.models import load_model


parser = argparse.ArgumentParser(description='17 flowers inference')

parser.add_argument('--data', type=str, help='data path, Ex: /data/img.jpg', default='/content/drive/MyDrive/datasets/Inference/flowers/01.jpg')
parser.add_argument('--model', type=str, help='model path', default='/content/drive/MyDrive/models/17-flowers/46_17_flowers_VGG16.h5')

args = parser.parse_args()

model = load_model(args.model)

img = cv2.imread(args.data)
img = cv2.cvtColor(img, (img, cv2.COLOR_BGR2GRAY))
img = cv2.resize(img, (width, height))
img = img/255.0
img = img.reshape(1, width, height, 3)
result = np.argmax(model.predict(img))
print(result)