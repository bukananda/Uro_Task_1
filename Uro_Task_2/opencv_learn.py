import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

# blank[:] = 0,255,0
# cv.imshow('Green',blank)
# cv.waitKey(0)

# img = cv.imread('human.jpg')
# cv.imshow('human',img)
# cv.waitKey(0)
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

video = cv.VideoCapture(0)

while True:
    isTrue, frame = video.read()

    flip = cv.flip(frame, 1)
    blank = np.zeros(flip.shape[:2], dtype='uint8')
    cv.imshow('flip',flip)
    cv.imshow('blank',blank)
    # frame_resize = rescaleFrame(flip)
    cvt_gray = cv.cvtColor(flip, cv.COLOR_BGR2GRAY)
    # cvt_hsv = cv.cvtColor(flip, cv.COLOR_BGR2HSV)
    # cvt_rgb = cv.cvtColor(flip, cv.COLOR_BGR2RGB)
    blur = cv.GaussianBlur(cvt_gray, (5,5), cv.BORDER_DEFAULT)
    # ret, thres = cv.threshold(cvt_gray, 125, 255, cv.THRESH_BINARY)
    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(blur, scaleFactor=1.1, minNeighbors=6)
    mask = cv.rectangle()
    for (x,y,w,h) in faces_rect:
        cv.rectangle(flip, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.imshow('Detected Faces', flip)
    # canny = cv.Canny(blur, 125, 175)
    # cv.imshow('thres',thres)
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