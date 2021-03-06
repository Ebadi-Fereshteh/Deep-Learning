# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Sxi7EtacSKtqyqdUR_ofwujyhIa6sYr
"""

import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout


class ExpertNet(Model):
  def __init__(self):
    super().__init__()

    self.dense_1 = Dense(128, activation="relu")
    self.dense_2 = Dense(64, activation="relu")
    self.dense_3 = Dense(14, activation="softmax")
    self.conv2d_1 = Conv2D(32, (3, 3), activation="relu", input_shape=(width,height,3))
    self.conv2d_2 = Conv2D(64, (3, 3), activation="relu")
    self.conv2d_3=Conv2D(128,(3,3),activation='relu')
    self.conv2d_4=Conv2D(256,(3,3),activation='relu')
    self.flatten = Flatten()
    self.maxpooling = MaxPooling2D
    self.dropout = Dropout(0.1)

  def call(self,x):
    L1= self.conv2d_1(x)  
    p1= self.maxpooling(L1)
    L2= self.conv2d_2(p1)
    p2= self.maxpooling(L2)
    L3= self.conv2d_3(p2)
    p3= self.maxpooling(L3)
    L4= self.conv2d_4(p3)
    p4= self.maxpooling(L4)
    L5= self.flatten(p4)
    L6= self.dense_1(L5)
    d1= self.droupout(L6)  
    L7= self.dense_2(d1)
    out= self.dense_3(L7)
    return out

