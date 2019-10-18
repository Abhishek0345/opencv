import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("tracking")
cv2.createTrackbar("l_h","tracking",0,255,nothing)
cv2.createTrackbar("l_s","tracking",0,255,nothing)
cv2.createTrackbar("l_v","tracking",0,255,nothing)
cv2.createTrackbar("u_h","tracking",255,255,nothing)
cv2.createTrackbar("u_s","tracking",255,255,nothing)
cv2.createTrackbar("u_v","tracking",255,255,nothing)
while(1):
    image = cv2.imread('multi.png')
   # cv2.imshow('image',image)
    #cv2.waitKey(5000)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lh =cv2.getTrackbarPos("l_h","tracking")
    ls=cv2.getTrackbarPos("l_s","tracking")
    lv=cv2.getTrackbarPos("l_v","tracking")
    uh=cv2.getTrackbarPos("u_h","tracking")
    us=cv2.getTrackbarPos("u_s","tracking")
    uv=cv2.getTrackbarPos("u_v","tracking")
    lb=np.array([lh,ls,lv])
    ub=np.array([uh,us,uv])
    mask = cv2.inRange(hsv,lb,ub)
    res = cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('image',image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break


cv2.destroyAllWindows()
