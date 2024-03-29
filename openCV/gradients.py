import cv2 as cv
import numpy as np

img = cv.imread("images/above.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Using the laplacian:
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

# sobel:
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("x", sobelx)
cv.imshow("combined", cv.bitwise_or(sobelx, sobely))

canny = cv.Canny(img, 150, 175)
cv.imshow("Canny", canny)

cv.waitKey(13000)