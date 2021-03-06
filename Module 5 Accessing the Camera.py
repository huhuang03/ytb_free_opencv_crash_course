import cv2
import os
import sys

PREVIE = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCornoers = 500,
                      qualityLevel = 0.2,
                      minDistance = 15,
                      blockSize = 9)

s = 0

if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)


win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)
