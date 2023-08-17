import cv2 as cv
# read and resize images and videos



img = cv.imread("images/aurora.png")
cv.imshow("aurora", img)

def rescaleFrame(frame, scale=.5):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimentions = (width, height)

	return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('images/vid.MOV')

while True:
	isTrue, frame = capture.read()

	frame_resized = rescaleFrame(frame)

	cv.imshow('Video', frame_resized)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break

cv.waitKey(0)

