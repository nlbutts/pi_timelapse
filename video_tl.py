#!/usr/bin/python

import picamera
import time
import os

def main():
	# Create a directory for the current time
	os.chdir('/home/pi/projects/pi_timelapse')
	dir = time.strftime('%Y_%m_%d_%H_%M_%S')
	#print('Creating directory ' + dir)
	os.mkdir(dir)
	os.chdir(dir)
	
	camera = picamera.PiCamera()
	counter = 0;
	while True:
		camera.annotate_background = picamera.Color('black')
		camera.annotate_text = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		filename = 'img{0:06d}.jpg'.format(counter)
		img = camera.capture(filename)
		counter = counter + 1
		#print('Captured ' + filename)
		# Capture once an hour
		time.sleep(60*10)
		#time.sleep(5)

if __name__ == "__main__":
	print('Starting Time lapse recorded')
	main()
