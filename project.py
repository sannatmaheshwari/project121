import cv2 
import numpy as np

video = cv2.VideoCapture(0)
image = cv2.imread("")
while True:
    ret,frame = video.read()
    frame = cv2.resize(frame,(640,480))
    image = cv2.resize(image,(640,480))
    u = np.array([104,153,70])
    l = np.array([30,30,0])
    m = cv2.inRange(frame,l,u)
    r = cv2.bitwise_and(frame,frame,mask = m)
    f = frame-r
    f = np.where(f==0,image,f)
    cv2.imshow("video",frame)
    cv2.imshow("mask",f)
    if cv2.waitKey(20)==32:
        break
video.release()
cv2.destroyAllWindows()