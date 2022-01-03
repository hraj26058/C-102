import cv2

def take_pictures():
	cvo=cv2.VideoCapture(0)
	results=True 
	while (results):
		ret,frame=cvo.read()
		cv2.imwrite("Image1.jpg",frame)
		results=False
	cvo.release()
	cv2.destroyAllWindows()
take_pictures()

		