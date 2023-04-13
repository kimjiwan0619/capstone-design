import os

import cv2

# 동영상 불러오기
capture = cv2.VideoCapture(0)
if not capture.isOpened(): raise Exception("카메라 연결 안됨")

# frames = []
filepath = './images/video_file.avi'

# 디렉토리 생성
try:
	if not os.path.exists(filepath[:-4]):
		os.makedirs(filepath[:-4])
except OSError:
	print('Error: Creating directory. ' +  filepath[:-4])

count = 0
max = 30

# 동영상 출력
while True:
	ret, frame = capture.read()
	if not ret: break

	# frames.append(frame)

	cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % (count % max), frame)
	print('Saved frame number :', str(int(capture.get(1))))
	count += 1

	# print(frame)
