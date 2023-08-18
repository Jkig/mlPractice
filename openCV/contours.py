import cv2 as cv
import numpy as np

img = cv.imread('images/sunset.png')

# cv.imshow("reg", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

cannyG = cv.Canny(gray, 125, 175)
canny = cv.Canny(img, 125, 175)
cannyBlur = cv.Canny(blur, 125, 175)
# cv.imshow("edgesG", cannyG)
# cv.imshow("edges", canny)
cv.imshow("edges-blur", cannyBlur)


# contoursG, hierarchiesG = cv.findContours(cannyG, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours, hierarchies = cv.findContours(cannyBlur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# other chain approx:
# print(f"{len(contoursG)} contours ( in Grayscale) found")
print(f"{len(contours)} contours found")

# cv.imshow("contours", contours)

# try threshold instead
ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contours found by threshold")


# look at threshold contors
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("threshContours", blank)
cv.waitKey(0)