# -*- coding: utf-8 -*-
"""SheykhDetector_Inference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UMWouvNMW_19XjGLozkWZH8cfRDSMlPX
"""

import argparse
import cv2
import numpy as np
from tensorflow.keras.models import load_model

from google.colab import drive
drive.mount("/content/drive/")

model = load_model('/content/drive/MyDrive/models/SheykhDetector_epoch_16.h5')

parser = argparse.ArgumentParser(description='SheykhDetector inference')
parser.add_argument('--data', type=str, help='data path, Ex: /data/img.jpg', default='/content/drive/MyDrive/datasets/Inference/SheykhRecognition/trump_01.png')

args = parser.parse_args()

image = cv2.imread(args.data)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (width, height))
image = image / 255
image = image.reshape(1, width, height, 3)  # 3d -> 4D

result = model.predict(image)
print(result)
pred = np.argmax(result)

if(pred == 0):
  print("Normal 👨 / 👩")
elif(pred == 1):
  print("Sheykh 👳")