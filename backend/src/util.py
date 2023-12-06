import cv2
import numpy as np

def preprocess_image(img):
    # Prepocessing image for better visibility
    gray = cv2.cvtColor(np.array(img), 
                        cv2.COLOR_BGR2GRAY)   
    resized = cv2.resize(gray, 
                         None, 
                         fx=2, 
                         fy=2, 
                         interpolation=cv2.INTER_LINEAR) 
    processed_img = cv2.adaptiveThreshold(resized, 
                                          255, 
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 
                                          61, 
                                          11) 
    return processed_img