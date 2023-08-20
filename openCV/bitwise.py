import cv2 as cv
import numpy as np


blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("bitand", cv.bitwise_and(rectangle, circle))
cv.imshow("bitor", cv.bitwise_or(rectangle, circle))
cv.imshow("bitxor", cv.bitwise_xor(rectangle, circle))

# bitwise not
cv.imshow("not", cv.bitwise_not(cv.bitwise_xor(rectangle, circle)))

img = cv.imread("images/cti.png")
# cv.imshow("reg", img)

cv.waitKey(3000)