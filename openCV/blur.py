import cv2 as cv

img = cv.imread("images/above.png")
cv.imshow("reg", img)

gBlur = cv.GaussianBlur(img, (9,9), 0)
cv.imshow("blur", gBlur)

ave = cv.blur(img, (9,9))
cv.imshow("aveBlur", ave)

median = cv.medianBlur(img, 9)
cv.imshow("medianBlur", median)

# the idea is keeping the edges but still blurring
# not really getting any effects i'm liking
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow("bi", bilateral)

cv.waitKey(0)