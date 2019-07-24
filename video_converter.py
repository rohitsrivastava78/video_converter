#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:10:33 2019

@author: rohit
"""

import cv2
import numpy as np

source_file='color_object1.avi'
out_file='color_object1.mp4'
fps=10


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(source_file)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))  

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(out_file,cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
video_write_config=False

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:        
    
    # Write the frame into the file 'output.avi'
    out.write(frame)
    
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press esc on keyboard to  exit
    if cv2.waitKey(10) == 27:
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()