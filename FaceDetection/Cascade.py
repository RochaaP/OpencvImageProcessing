import cv2
import numpy as np



face = cv2.CascadeClassifier('frontalface.xml')				
eye = cv2.CascadeClassifier('eye.xml')

cap = cv2.VideoCapture(0)					#Default web camera
#cap = cv2.VideoCapture(1)					#USB or second web camera
#cap = cv2.VideoCapture('fileName')				#using separate video



while True:
	ret, img = cap.read()
	gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 	faces = face.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye.detectMultiScale(roi_gray)
		for(ex, ey,ew, eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ey, ey+eh),(0,255,0),2)


	cv2.imshow('img',img)
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

