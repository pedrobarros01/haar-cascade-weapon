import cv2
import matplotlib.pyplot as plt


def cascade():
    cascade = cv2.CascadeClassifier('classifier/cascade.xml')

    test_image = "src/images/p/knife_9.jpg"
    img = cv2.imread(test_image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    objects = cascade.detectMultiScale(gray, 2.5, 13)

    for (x, y, w, h) in objects:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()
