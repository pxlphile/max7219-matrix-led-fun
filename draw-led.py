#!/usr/bin/env python

import max7219.led as led
import time
import sys

# define x,y matrix resolution in pixel
resolution = [8,8]
maxX = resolution[0]
maxY = resolution[1]
device = None

picture = [\
	[0,0,0,0,0,0,0,0],\
        [0,0,1,0,0,0,1,0],\
        [0,1,0,1,0,1,0,1],\
        [0,0,0,0,0,0,0,0],\
        [0,0,0,0,0,0,0,0],\
        [0,1,0,0,0,0,0,1],\
        [0,0,1,0,0,0,1,0],\
        [0,0,0,1,1,1,0,0]]

def run():
	global device
	device = led.matrix(cascaded=1)
	drawBitmap()
	time.sleep(10)

def drawBitmap():
	for currentY in range(maxY):
		drawLine(currentY)
	device.flush()

def drawLine(currentY):
	for currentX in range(maxX):
		shouldDraw = resolveBitmapAt(currentX, currentY)
		if shouldDraw:
			device.pixel(currentX, currentY, 7, redraw=False)

def resolveBitmapAt(currentX, currentY):
	if picture[currentY][currentX] == 1:
		return True
	return False

def cleanUp():
	device.show_message(" ")

def main():
	try:
		run()
		cleanUp()
	except KeyboardInterrupt:
		print "Exiting..."
		cleanUp()
		sys.exit(0)

if __name__ == "__main__":
	main()
