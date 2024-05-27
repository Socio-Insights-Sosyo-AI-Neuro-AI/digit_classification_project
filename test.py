
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon, QPixmap, QImage, QPainter, QPen # icon and load image
from PyQt6.QtCore import Qt, QPoint

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # load image

import cv2 # open-cv use for image resize

## Convolutional Neural Network
import keras
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

#%% preprocess

(x_train, y_train),(x_test, y_test) = mnist.load_data()

plt.figure()
i = 55
plt.imshow(x_train[i], cmap = "gray")
print("Label: ",y_train[i])
plt.axis("off")
plt.grid(False)

img_rows = 28
img_cols = 28
x_train = x_train.reshape( x_train.shape[0],img_rows,img_cols,1)
x_test = x_test.reshape( x_test.shape[0],img_rows,img_cols,1)
input_shape = (img_rows,img_cols,1)




#normalize
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

x_train /= 255 # x_train = x_train/255
x_test /= 255

num_classes = 10
y_train = keras.utils.to_categorical(y_train,num_classes)
y_test = keras.utils.to_categorical(y_test,num_classes)

