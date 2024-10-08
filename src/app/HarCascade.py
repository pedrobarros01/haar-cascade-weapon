import cv2
import matplotlib.pyplot as plt


def cascade_video(path_classifier, path_video):
    cascade = cv2.CascadeClassifier(path_classifier)
    video = cv2.VideoCapture(path_video)
    while True:
        ret, img = video.read()
        if not ret: 
            print("Frame final do vídeo")
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        objects = cascade.detectMultiScale(gray,3.5, 25)

        for (x, y, w, h) in objects:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('frame', img)
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord('x'):
            break
    video.release()
    cv2.destroyAllWindows()