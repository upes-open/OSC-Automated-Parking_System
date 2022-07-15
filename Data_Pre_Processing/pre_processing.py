import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt

def grey(img): #grascayling the image
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  
    return gray

def sharpen(image): #sharpening the image
    kernel = np.array([[0, -1, 0],[-1, 5,-1],[0, -1, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    return image_sharp

def contour(gimage): # detect contour
    _, binary = cv2.threshold(gimage, 225, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.drawContours(gimage, contours, -1, (0, 255, 0), 2)
    return image

def histeq(img): #Histogram equalization
    equ = cv2.equalizeHist(img)
    return equ

i = 0
for img in glob.glob("Data_Extraction/Images/*.jpg"): #loading images from folder
    cv_img = cv2.imread(img)  #reading the image
    image = sharpen(cv_img) #sharpen the image
    gimage = grey(image) #grayscaling the image
    himage = histeq(gimage) #histogram equalizing the image
    image = contour(himage)
    cv2.imwrite(f"Data_Extraction/processed_images/{i}.jpg", himage) #saving it 
    i = i + 1
    
    
    
