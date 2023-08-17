import cv2 as cv

img = cv.imread("images/cit.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("color", img)
cv.imshow("grayscale", gray)

cv.waitKey(10000)