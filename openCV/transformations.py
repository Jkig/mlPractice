import cv2 as cv
import numpy as np

img = cv.imread("images/winter.png")
cv.imshow("reg", img)

# translate:
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

translated = translate(img, 100, -100)
# cv.imshow("translated", translated)

# rotation:
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint == None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)
    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img, -30)
# cv.imshow("rot", rotated)

# resizing:
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("resized", resized)

# flip:

flip = cv.flip(img, -1)
cv.imshow("flipped", flip)

cv.waitKey(5000)