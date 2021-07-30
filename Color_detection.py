#pyhton code color detection
import numpy as np 
import cv2 

def color_detection(cap):
    #lower value(hsv) of colors
    colors_lower =[[0,100,10],[10,100,10],[20,100,10],
        [35,100,10],[75,10,10],[130,10,10],[150,10,10],[170,10,10]]
    #upper
    colors_upper =[[10,255,255],[20,255,255],[35,255,255],
        [75,255,255],[130,255,255],[150,255,255],[170,255,255],[180,255,255]]

    color_name =['red','orange','yellow','green','blue','purple','pink','red']

    while(cap.isOpened):
        _,frame =cap.read()
        #convert bgr to hsv
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        #detect colors of frame
        for i in range(len(colors_lower)) :
            color_lower =np.array(colors_lower[i],np.uint8)
            color_upper =np.array(colors_upper[i],np.uint8)
            color_mask = cv2.inRange(hsvFrame, color_lower, color_upper) 
            contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
            for pic, contour in enumerate(contours): 
                area = cv2.contourArea(contour) 
                if(area > 100):
                    x, y, w, h = cv2.boundingRect(contour) 
                    cv2.putText(frame, color_name[i], (x, y), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255))	
        cv2.imshow("Color Detection", frame) 
        if cv2.waitKey(10) & 0xFF == ord('q'): 
            break
        
    cap.release() 
    cv2.destroyAllWindows() 
cap = cv2.VideoCapture('A.mp4') 
color_detection(cap)