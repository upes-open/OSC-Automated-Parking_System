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
i = 0
for img in glob.glob("Data_Extraction/Images/*.jpg"): #loading images from folder
    cv_img = cv2.imread(img)  #reading the image
    image = sharpen(cv_img) #sharpen the image
    image = grey(image) #grayscaling the image
    cv2.imwrite(f"Data_Extraction/processed_images/{i}.jpg", image) #saving it 
    i = i + 1