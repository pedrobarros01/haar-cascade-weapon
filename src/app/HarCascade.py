import cv2
import matplotlib.pyplot as plt


def cascade_video():
    cascade = cv2.CascadeClassifier('classifier/cascade.xml')
    video = cv2.VideoCapture('src/images/video/video.mp4')
    while True:
        ret, img = video.read()
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        objects = cascade.detectMultiScale(gray,1.2, 12)

        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('frame', img)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord('x'):
            break
    video.release()
    cv2.destroyAllWindows()