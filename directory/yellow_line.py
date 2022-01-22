import cv2
import numpy as np

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
classes = []
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

img = cv2.imread('image.jpg')
height, width, _= img.shape

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()