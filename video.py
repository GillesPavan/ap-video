#Inspired by :
#https://www.pyimagesearch.com/

# import the necessary packages
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
ap.add_argument("-c", "--contour", action='store_true', required=False,
	help="adds contours to the image")
ap.add_argument("-t", "--threshold", required=False,
	help="contour threshold, from 0 to 255, default=30")
args = vars(ap.parse_args())
 
# open a pointer to the video stream and start the FPS timer
stream = cv2.VideoCapture(args["video"])
fps = FPS().start()

written = False

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video file stream
	(grabbed, frame) = stream.read()
 
	# if the frame was not grabbed, then we have reached the end
	# of the stream
	if not grabbed:
		break
 
	# resize the frame and convert it to grayscale 
	frame = imutils.resize(frame, width=450)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	if written == False :
		cv2.imwrite("frame.jpg", frame)
	written = True
	
	# show the frame and update the FPS counter
	cv2.imshow("Frame", frame)
	cv2.waitKey(10)
	fps.update()