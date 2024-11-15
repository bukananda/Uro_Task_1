import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    # blank = np.zeros((500,500,3), dtype='uint8')
    isTrue, frame = video.read()

    flip = cv.flip(frame, 1)
    cv.imshow('flip',flip)
    # frame_resize = rescaleFrame(flip)
    cvt_gray = cv.cvtColor(flip, cv.COLOR_BGR2GRAY)
    # cvt_hsv = cv.cvtColor(flip, cv.COLOR_BGR2HSV)
    # cvt_rgb = cv.cvtColor(flip, cv.COLOR_BGR2RGB)
    blur = cv.GaussianBlur(cvt_gray, (5,5), cv.BORDER_DEFAULT)
    ret, thres = cv.threshold(cvt_gray, 125, 255, cv.THRESH_BINARY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=6)
    for (x,y,w,h) in faces_rect:
        cv.rectangle(flip, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.imshow('Detected Faces', flip)
    # canny = cv.Canny(blur, 125, 175)
    cv.imshow('thres',thres)
    # contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv. CHAIN_APPROX_SIMPLE)
    # cv.drawContours(blank,contours, -1, (0,0,255), 2)
    # cv.imshow('Contour_drawn', blank)
    # cv.imshow('human2',cvt_rgb)
    # cv.imshow('resize',frame_resize)
    # cv.imshow('blur',blur)
    # cv.imshow('canny',canny)
    # print(len(contours))

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()