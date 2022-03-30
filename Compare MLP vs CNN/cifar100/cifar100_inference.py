# -*- coding: utf-8 -*-
"""cifar100-inference.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/143hriXha0Qq0Xhb7_LOBdv2WnXrbVrcx
"""

import argparse
import cv2
import numpy as np
from tensorflow.keras.models import load_model


parser = argparse.ArgumentParser(description='cifar100 inference')

parser.add_argument('--data', type=str, help='data path, Ex: /data/img.jpg', default='test_image.jpg')
parser.add_argument('--model', type=str, help='select the model: mlp | cnn', default='cnn')

args = parser.parse_args()

if args.model == 'cnn':
    model = load_model('cnn-mlp-cifar100.h5')
else
    model = load_model('mlp-cifar100.h5')

img = cv2.imread(args.data)
img = cv2.resize(img, (32, 32))
img = cv2.cvtColor(img, (img, cv2.COLOR_BGR2GRAY))
img = img/255.0
img = img.reshape(32, 32, 3)

result = np.argmax(model.predict(img))
print(result)