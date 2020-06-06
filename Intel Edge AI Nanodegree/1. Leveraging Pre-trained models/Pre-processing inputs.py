import cv2
import numpy as np

def pose_estimation(input_image):
    preprocessed_image = np.copy(input_image)
    return cv2.resize(preprocessed_image, (456,256)).transpose(2,0,1).reshape(1,3,256,456)

def text_detection(input_image):
    preprocessed_image = np.copy(input_image)
    return cv2.resize(preprocessed_image, (1289,768)).transpose(2,0,1).reshape(1,3,768,1280)

def car_meta(input_image):
    preprocessed_image = np.copy(input_image)
    return cv2.resize(preprocessed_image, (72,72)).transpose(2,0,1).reshape(1,3,72,72)