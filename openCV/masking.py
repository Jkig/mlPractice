import cv2 as cv
import numpy as np


img = cv.imread("images/winter.png")

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 760, 255, -1)
cv.imshow("masked", cv.bitwise_and(img, img, mask=circle))

rect = cv.rectangle(blank.copy(),(img.shape[1]//2-10, 0), (img.shape[1]//2+10, img.shape[0]), 255, -1)
rect = cv.rectangle(rect,(0, img.shape[0]//2-10), (img.shape[1], img.shape[0]//2+10), 255, -1)

cv.imshow("Borders Masked", cv.bitwise_and(img, img, mask=cv.bitwise_not(rect)))

cv.waitKey(6000)