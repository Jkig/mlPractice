import cv2 as cv
import numpy as np

# blank image:
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('images/winter.png')
# cv.imshow("winter", img)

# draw a square:
# blank[200:300, 300:400] = 0,255,0
# cv.imshow("green", blank)

# rectangle:
# cv.rectangle(blank, (250,0), (250,500), (255,255,0), thickness=2)
# cv.imshow("rect", blank)

# lines
# img = cv.imread("images/sunset.png")
# cv.line(img, (img.shape[1]//2, 0), (img.shape[1]//2, img.shape[0]), (0,0,0), thickness=2)
# cv.line(img, (0, img.shape[0]//2), (img.shape[1], img.shape[0]//2), (0,0,0), thickness=2)
# cv.imshow("Sunset", img)


cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 25, (0,0,255), thickness=2)
cv.line(blank, (blank.shape[1]//2, 0), (blank.shape[1]//2, blank.shape[0]), (255,0,0), thickness=2)
cv.line(blank, (0, blank.shape[0]//2), (blank.shape[1], blank.shape[0]//2), (0,255,0), thickness=2)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 5, (255,255,255), thickness=-1)

cv.putText(blank, "Hello world", (255,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)

cv.imshow("drawings", blank)
cv.waitKey(10000)