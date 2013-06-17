import cv2, cv2.cv as cv

cv2.namedWindow("camera", 1)
capture = cv2.VideoCapture(0)
#
width=int(capture.get(cv.CV_CAP_PROP_FRAME_WIDTH))
height=int(capture.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
fps=25.0
#
vwriter = cv2.VideoWriter("copy.avi", 0, fps, (width, height))
while True:
    ret, img = capture.read()
    vwriter.write(img)
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
        break
capture.release()
cv2.destroyWindow("camera")
