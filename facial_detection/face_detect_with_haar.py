import cv2 as cv

img = cv.imread("../openCV/images/smile.jpeg")
# got some false positives for dude.jpeg
# and it obvisouly doesn't work for profile angle of faces
# really cool thing for the smile.jpeg, is that when you look at false
#   positives, you can often kinda see it
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h),(0,255,0), 2)

cv.imshow("detected", img)

cv.waitKey(10000)