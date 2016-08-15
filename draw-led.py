#!/usr/bin/env python

import max7219.led as led
import time
import sys

def run():
#	device = led.matrix(cascaded=1)
	print "hello world"
#	device.pixel(4, 4, 1, redraw=False)
#	device.flush()
	time.sleep(10)

def main():
	try:
		run()
	except KeyboardInterrupt:
		print "Exiting..."
		sys.exit(0)

if __name__ == "__main__":
	main()
