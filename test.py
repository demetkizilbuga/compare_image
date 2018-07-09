from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread("1.jpeg")
img2 = cv2.imread("2.jpg")
        
img11 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img12 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
imageA = cv2.resize(img11, (100, 100)) 
imageB = cv2.resize(img12, (100, 100)) 
        
s = ssim(imageA, imageB)

print(s)
