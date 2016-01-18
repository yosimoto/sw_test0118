#!/usr/bin/python

from SimpleCV import Image, Camera, Display,DrawingLayer,Color
from time import sleep, time
import random
import RPi.GPIO as GPIO

myCamera = Camera(prop_set={'width':320,'height':240})
myDisplay = Display(resolution=(320,240))
myDrawingLayer = DrawingLayer((320,240))

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

while not myDisplay.isDone():
	frame = myCamera.getImage()
	faces = frame.findHaarFeatures('face')
	if faces:
		for face in faces:
			GPIO.output(2,GPIO.HIGH)
			print "Face at: " + str(face.coordinates())
			
			
			frame.clearLayers()
			myDrawingLayer.rectangle((0,0),(120,30),filled=True)
			myDrawingLayer.setFontSize(45)
			myDrawingLayer.text(`random.randint(1,1000000)`,(0,0),color=Color.RED)
			
			frame.addDrawingLayer(myDrawingLayer)
			frame.save("combat power" + str(time()) + ".jpg")
			sleep(.3)
	else:
		print"NO face"
	
	GPIO.output(2,GPIO.LOW)
	frame.save(myDisplay)	
	sleep(.1)
