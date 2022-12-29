import cv2 
import numpy as np 
import time
import datetime
# Create a VideoCapture object 
cap = cv2.VideoCapture(1) 
# Capture a frame ret, img = cap.read() 
# Release the capture cap.release()


nframes = 1024
interval = 10

for i in range(nframes):
    # capture
    ret, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(datetime.datetime.now()),(120,200), font, 1,(255,255,255),2)

    # save file 
    cv2.imwrite('./img_'+str(i).zfill(4)+'.png', img)
    # wait 5 seconds
    time.sleep(interval)

def create_video():
    print ('\nCreating video.\n')
    os.system('avconv -framerate 20 -i ' + dir + '/image%08d.jpg -vf format=yuv420p ' + dir + '/timelapse.mp4')  # noqa
