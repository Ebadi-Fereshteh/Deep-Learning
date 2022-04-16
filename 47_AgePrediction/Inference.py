# -*- coding: utf-8 -*-
"""AgePredictionInference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZP3KPyDBMy2cMLqpiL5jBabxpdyw60uZ
"""

import argparse
import cv2
import numpy as np
from tensorflow.keras.models import load_model


parser = argparse.ArgumentParser(description='Age Prediction inference')

parser.add_argument('--data', type=str, help='data path, Example: /data/03.png', default='03.png')
parser.add_argument('--model', type=str, help='select the model: ResNetV2 | MobileNetV2 | Xception', default='Xception')

args = parser.parse_args()

if args.model == 'ResNetV2':
    model = load_model('AgePrediction_Resnet2_19.h5')
elif args.model == 'MobileNetV2':
    model = load_model('AgePrediction_mobilenet2V2.h5')
elif args.model == 'Xception':
    model = load_model('AgePrediction_xception2_19.h5')

image=cv2.imread(args.data)
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image=cv2.resize(image,(width,height))
image=image/255.0
image=image.reshape(1, width, height, 3)
result=model.predict(image)
print(result)