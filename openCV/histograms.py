import cv2 as cv
import numpy as np


img = cv.imread("images/above.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

cv.waitKey(6000)