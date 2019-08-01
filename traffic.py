import cv2 as cv
import numpy as np

'''
Function to detect traffic signals - red and green.
Takes the source image as input and looks for red and
green circles in the image.

input - src - source image
return values - 0 - red
                1 - green
'''
def traffic_signal(src)
        src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
        kernel = np.ones((5, 5))

        #red
        r_lower = np.array([-3, 91, 215])   
        r_upper = np.array([17, 111, 295]) 
        redmask = cv.inRange(src_hsv, r_lower, r_upper)
        red_edges = cv.Canny(redmask, 75, 150)
        red_edges = cv.dilate(red_edges, kernel, iterations = 1)

        r_circle = cv.HoughCircles(red_edges, 
                                   cv.HOUGH_GRADIENT, 1,
                                   red_edges.shape[0]/20,
                                   param1 = 6, 
                                   param2 = 3, 
                                   minRadius = 0, 
                                   maxRadius = 20)

        if r_circle is not None:
               return 0;
        else:
                #green
                g_lower = np.array([50, 36, 214])   
                g_upper = np.array([70, 56, 294]) 
                greenmask = cv.inRange(src_hsv, g_lower, g_upper)
                green_edges = cv.Canny(greenmask, 75, 150)
                green_edges = cv.dilate(green_edges, kernel, iterations = 1)

                g_circle = cv.HoughCircles(green_edges, 
                                           cv.HOUGH_GRADIENT, 1, 
                                           green_edges.shape[0]/20, 
                                           param1 = 6, 
                                           param2 = 3, 
                                           minRadius = 0, 
                                           maxRadius = 20)

                if g_circle is not None:
                        return 1;


