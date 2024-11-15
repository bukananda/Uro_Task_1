import cv2

def rescaleFrame(frame, scale = 1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

tracker = cv2.TrackerKCF_create()
init_box = None
video = cv2.VideoCapture(0)

ok, frame = video.read()
if ok:
    init_box = cv2.selectROI(cv2.flip(rescaleFrame(frame),1), False)
    tracker.init(frame, init_box)
while True:
    ok, frame = video.read()
    resize_flip = cv2.flip(rescaleFrame(frame),1)
    if not ok:
        break
    ok, bbox = tracker.update(resize_flip)
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(resize_flip, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    else:
        cv2.putText(resize_flip, "Tracking failure", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    cv2.imshow("Tracking", resize_flip)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()