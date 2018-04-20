from picamera import PiCamera
from time import sleep

cam = PiCamera()
cam.resolution = (1024, 768)    //…Ë÷√∑÷±Ê¬ 
cam.start_preview()
for i in range(10):
    sleep(3)
    cam.capture('/home/pi/photo/image%y%M%D%h%s.jpg'%i)
cam.stop_preview()
