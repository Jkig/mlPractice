import cv2 as cv

img = cv.imread("images/above.png")

blur = cv.GaussianBlur(img, (19,1), cv.BORDER_DEFAULT)
# blur2 = cv.GaussianBlur(img, (19,19), cv.BORDER_DEFAULT)

cv.imshow("reg", img)
cv.imshow("blur", blur)
# cv.imshow("blur2", blur2)

cv.waitKey(10000)