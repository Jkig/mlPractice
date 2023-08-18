import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images/aurora.png")
cv.imshow("Regular", img)

# to gray:
# cv.imshow("gray", cv.cvtColor(img, cv.COLOR_BGR2GRAY))

# BGR to HSV:
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# BGR to LAB:
# cv.imshow("LAB", cv.cvtColor(img, cv.COLOR_BGR2LAB))

# Note that everyone else uses RGB ofcourse, lol
# why do it this way openCV??
# i'm sure legacy tech when we only had blue and green screens or something silly
plt.imshow(img)

# convert to normal color for others:
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
# plt.show()

# try some cross transfomrations:
# cv.imshow("bgr", cv.cvtColor(hsv, cv.COLOR_HSV2BGR))

# Gray back to color:
cv.imshow("colorfromGray", cv.cvtColor(cv.cvtColor(img, cv.COLOR_BGR2GRAY), cv.COLOR_GRAY2BGR))
# ok so gray does actually destroy the info, but LAB,HSV, BGR, RGB are all the same (probs most others too)


cv.waitKey(0)