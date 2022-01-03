import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
	number=random.randint(0,1000)
	cvo=cv2.VideoCapture(0)
	results=True
	while (results):
		ret,frame=cvo.read()
		img_name="Img"+str(number)+".png"
		cv2.imwrite(img_name,frame)
		start_time=time.time()
		results=False
	return img_name
	print("Snapshot was taken")
	cvo.release()
	cv2.destroyAllWindows()
def upload_file(img_name):
	access_token='bssSOBkyHBwAAAAAAAAAASpb3GFxjNCNrfYkPOC5Qnu0U6cylN7sFa74XyKPsUdd'
	file=img_name
	file_from=file
	file_to="/test1/"+img_name
	dbx=dropbox.Dropbox(access_token)
	with open(file_from,'rb') as f:
		dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
		print("File uploaded")
def main():
	while (True):
		if((time.time()-start_time) >= 5):
			name=take_snapshot()
			upload_file(name)
main()
