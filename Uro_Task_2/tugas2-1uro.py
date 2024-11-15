import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cap = cv.VideoCapture("object_video.mp4")

while True:

    isTrue, frame = cap.read()
    resize = rescaleFrame(frame)

    hsv = cv.cvtColor(resize, cv.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])    # Lower range of red
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])  # Upper range of red
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask = mask1|mask2

    canny = cv.Canny(mask, 125, 175)

    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv.contourArea(contour)
        if area > 300:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(resize, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("resize", resize)
    cv.imshow("Mask", mask)
    cv.imshow("canny", canny)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()