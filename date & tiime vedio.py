import cv2
import datetime
cap = cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('time.avi',fourcc,30.0,(640,480))
while(True):
    ret , frame = cap.read()
    if ret==True:
        font =cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        date1=str(datetime.datetime.now())
        frame =cv2.putText(frame,date1,(50,50),font,1,(255,156,32),2,cv2.LINE_8)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()