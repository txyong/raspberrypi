#! /usr/bin/env python
from picamera import PiCamera
from time import sleep
from datetime import datetime

#dtime = datetime.now().strftime('%Y%m%d_%H:%M:%S')
#print (dtime)
cam = PiCamera()
cam.resolution = (1024, 768)
cam.start_preview()
for i in range(5):
    sleep(3)
#    cam.capture('/home/pi/photo/image%d.jpg'%i)
#    cam.capture('Captured %s' % '/home/pi/photo/image.jpg')
#    for filename in cam.capture_continuous('img{timestamp:%Y%m%d%H%M%S}.jpg'):
#        'Captured %s' % filename
#        exit()
    dtime = datetime.now().strftime('%Y%m%d_%H:%M:%S')
    imgfile = open('/home/pi/photo/img' + dtime + '.jpg', 'w')
    cam.capture(imgfile)
    imgfile.close()
cam.stop_preview()
