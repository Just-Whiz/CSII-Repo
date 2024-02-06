from djitellopy import Tello
from time import sleep
import cv2

tello = Tello()

tello.connect()

tello.takeoff().sleep(2)
tello.send_rc_control(0, 50, 0, 30)
#tello.send_rc_control(0, 50, 0, 30)
tello.land()
