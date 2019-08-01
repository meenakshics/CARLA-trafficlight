import cv2 as cv
import traffic.py
#import numpy as np
#import sys

file_label = 5426
label_str = '00' + str(file_label) + '.png'
img = cv.imread(label_str)
while img is not None:
        flag = -1
        flag = traffic_signal(img)
        if(flag == 0):
                file_name = 'red/' + label_str
                cv.imwrite(file_name, img)

        else if(flag == 1):
                file_name = 'green/' + label_str
                cv.imwrite(file_name, img)
         
        flag += 1
        label_str = '00' + str(file_label) + '.png'
        img = cv.imread(label_str) 
