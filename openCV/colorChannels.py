import cv2 as cv
import numpy as np

img = cv.imread("images/winter.png")
cv.imshow("Basic", img)

b, g, r = cv.split(img)


# converts to grayscale where the color is white
# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)
# print(img.shape)
# print(b.shape)



# for normal
# cv.imshow("Merged", cv.merge([b,g,r]))

# can mix the colors up for cool effect, ex:
# cv.imshow("Merged", cv.merge([r,b,g]))
# cv.imshow("Merged", cv.merge([g,r,b]))


# try showing colors as what they actually are:
blank = np.zeros(img.shape[:2], dtype="uint8")
# cv.imshow("Blue", cv.merge([b, blank, blank]))
# cv.imshow("Green", cv.merge([blank, g, blank]))
# cv.imshow("Red", cv.merge([blank, blank, r]))

# now mix both
# cv.imshow("Red/blue", cv.merge([r, blank, blank]))
# cv.imshow("Red/blue", cv.merge([r, blank, b]))
# cv.imshow("Red/blue", cv.merge([b, blank, r]))
# cv.imshow("Red/blue", cv.merge([b, r, r]))

# what if I blur just one color:

# cv.imshow("Merged", cv.merge([b,cv.GaussianBlur(g, (9,9), 0),r]))
greenBlur = cv.GaussianBlur(g, (9,9), 0)
mixed = (greenBlur + g)//2

# cool effect, mix blured and regular
# cv.imshow("Green", cv.merge([blank, g, blank]))
# cv.imshow("greenblur", cv.merge([blank, greenBlur, blank]))
# cv.imshow("mixed", cv.merge([blank, mixed, blank]))
# cv.imshow("Merged", cv.merge([b,mixed,r]))

# same for everything:
cv.imshow("MergedAll", cv.merge([(cv.GaussianBlur(b, (9,9), 0) + b)//2,(cv.GaussianBlur(g, (9,9), 0) + g)//2,(cv.GaussianBlur(r, (9,9), 0) + r)//2]))
# I want to split each channnel into low colors and high colors
# then blur all the high colors??
# or seperate into pure colors and not, and blur the pure colors, then re merge

cv.waitKey(0)