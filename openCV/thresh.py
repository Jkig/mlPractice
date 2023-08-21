import cv2 as cv
import numpy as np

img = cv.imread("images/aurora.png")
# img = cv.imread("images/cit.png") # city looks really cool, almost there
cv.imshow("reg", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshVal = 100

threshold, thresh = cv.threshold(gray, threshVal, 255, cv.THRESH_BINARY)
# cv.imshow("Theshold", thresh)


blank = np.zeros(img.shape[:2], dtype='uint8')

onlyBright = cv.bitwise_and(img, img, mask=thresh)
cv.imshow("Bright Masked", onlyBright)
# cv.imshow("mixed mask", (onlyBright+img)//2)
# I need to mix better, maybe take max of either reg*.25 and threshhold masked
# recombine:
thresholdI, threshI = cv.threshold(gray, threshVal, 255, cv.THRESH_BINARY_INV)
onlyDark = cv.bitwise_and(img, img, mask=threshI)
# cv.imshow("recombined", onlyDark+onlyBright)
cv.imshow("recombined", onlyDark//3+onlyBright)

# adaptive
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 3)
cv.imshow("adaptive", adaptive_thresh)
cv.imshow("adaptivecolors", cv.bitwise_and(img, img, mask=adaptive_thresh))

cv.waitKey(13000)