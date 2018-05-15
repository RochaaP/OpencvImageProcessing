import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests

car = cv2.CascadeClassifier('cars.xml')					#haascascade file

cap = cv2.VideoCapture('Car.mp4')
# bgsMOG = cv2.createBackgroundSubtractorMOG2()
# fgbg = cv2.createBackgroundSubtractorMOG2()			#background-moving objects detect
bgsMOG = cv2.createBackgroundSubtractorMOG2()
count =0
while True:
	ret,img = cap.read()

	# fgmask = fgbg.apply(img, None, 0.9)
	gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# fgmask = fgbg.apply(gray)
	cars = car.detectMultiScale(gray, 	1.3 ,	3)
	# 							#image speed	detecting scale	

	cv2.line(img, (220, 300), (1100,300), (0,255,125), 8)
	# 			# starting		ending
				# point			point		color 		thickness
	
	for(x,y,w,h) in cars:
		# (x, y, w, h) = cv2.boundingRect(img)
		cv2.rectangle(img, (x,y),  		(x+w, y+h),	(255,0,0), 2)
					#image	starting 	ending 		color 	thikness
					#		point		point
		# roi_gray = gray[y:y+h, x:x+w]
		# roi_color = img[y:y+h, x:x+w]
		

		cv2.imshow('img',img)
		# cv2.imshow('fg',fgmask)

	

	if cv2.waitKey(5) & 0xFF == ord('q'):
		count +=1
		plt.imshow(img)
		plt.xticks([])
		plt.yticks([])
		cv2.imwrite('pic'+str(count)+'.jpg',img)
		plt.show()
		url = "https://drive.google.com/drive/folders/1Ug1mINXAhhC1VOwwMHUxNJ-Xc7zgJhgp?usp=sharing"
		files = {'file':open('pic'+str(count)+'.jpg','rb')}
		headers = {
					'authorization':"Bearer{token}"
				}
		respose = requests.post(url,files = files)
		cv2.imshow('img',img)
		
	
	if cv2.waitKey(10) == 27:
		break


	

cv2.destroyAllWindows()
cap.release()

