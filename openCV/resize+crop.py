import cv2 as cv

img = cv.imread("images/sunset.png")

cv.imshow("reg", img)

# width = 500
# ratio = (img.shape[0]*width)//img.shape[1]

# small = cv.resize(img, (width,ratio))
# cv.imshow("small", small)

piece = img[500:800, 500:800]
cv.imshow("piece", piece)

cv.waitKey(0)