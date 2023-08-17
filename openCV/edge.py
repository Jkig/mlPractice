import cv2 as cv

img = cv.imread("images/glow.png")


# cv.imshow("reg", img)

# canny = cv.Canny(img, 125, 125)
# cv.imshow("canny edge", canny)


# try to blur first:
# # blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# cannyBlur = cv.Canny(blur, 125, 125)

# cv.imshow("blur", blur)
# cv.imshow("canny", cannyBlur)


# Dilate:
# canny = cv.Canny(img, 125, 125)
# cv.imshow("canny edge", canny)
# dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow("dilated", dilated)

# now bring it back somewhat:
canny = cv.Canny(img, 125, 125)
cv.imshow("canny edge", canny)

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("dilated", dilated)

eroded = cv.erode(dilated, (9,9), iterations=1)
cv.imshow("eroded", eroded)

cv.waitKey(0)