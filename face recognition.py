#Find location of haarcascade_frontalface_default.xml
'''import os
import cv2

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
print(haar_model)
'''
#--------------------------------------


import cv2  #import computer vision libraries

cap = cv2.VideoCapture(r'C:\Users\asus\Downloads\vtest.mp4') # give location of video for using webcam use 0 in parameter
faceCascade=cv2.CascadeClassifier('D:\python\lib\site-packages\cv2\data/haarcascade_frontalface_default.xml')
#faceCascade class file to detect only the faces in build function   

while(True): #for every frame treat as a image
    sucess,frame = cap.read() #frame varriable will capture the video & sucess varriable will tell us whether it was captures sucess pr not
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #detection better 
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)  #rectangle perameter and location of perameters
    cv2.imshow("Video",frame)  #show the frame
    if(cv2.waitKey(1) == ord('q')): #this adds a Delay and looks for the key press inorder to break the loop
        cap.release()   #release the resourse safter recordings
        cv2.destroyAllWindows()
        break  #Press q for Quit

    

'''
import cv2

cv2.namedWindow("camera",1)
capture = cv2.VideoCapture()
capture.open(0)
while True:
    img = capture.read()[1]
    cv2.imshow("camera", img)
    cv2.waitKey(10)
cv2.destroyWindow("camera")
'''
