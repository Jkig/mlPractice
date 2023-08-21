import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread("images/above.png")

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])


colors = ('b', 'g', 'r')


plt.figure()
plt.title("Hist")
plt.xlabel("Bins")
plt.ylabel("# of pixles")

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist)
    plt.xlim([0,256])

plt.show()

cv.waitKey(6000)