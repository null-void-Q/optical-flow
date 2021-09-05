import numpy as np
import cv2

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)
time=cv2.getTickCount()
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
