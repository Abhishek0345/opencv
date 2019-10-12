import cv2
img = cv2.imread("lena.jpg")
cv2.line(img,(0,2),(510,510),(255,42,53),8)
img = cv2.circle(img,(255,255),100,(255,255,0),-1)
img = cv2.circle(img,(255,255),50,(0,255,255),-1)
img = cv2.rectangle(img,(205,285),(325,305),(255,0,255),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()