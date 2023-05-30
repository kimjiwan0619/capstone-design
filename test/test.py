# 1번째 텍스트 파일 읽기
file1_name = "video_test1" + ".txt"
file1 = open("../yolov8_tracking/runs/track/exp/tracks/" + file1_name, "r")
data1 = file1.readlines()
file1.close()

# 2번째 텍스트 파일 읽기
file2_name = file1_name + "_labeling_average.txt"
file2 = open("../labeling/result/" + file2_name, "r")
data2 = file2.readlines()
file2.close()

# 오차 계산을 위한 변수 초기화
missed_detection = 0
false_alarm = 0

data1_list = []
data2_list = []

for line in data1:
    frame_number, _, _, _, _, _= line.strip().split()
    if frame_number not in data1_list:
        data1_list.append(frame_number)

for line in data2:
    frame_number, OnOFF = line.strip().split()
    if OnOFF == "ON":
        data2_list.append(frame_number)

# 오차 계산
for frame_number in data2_list:
    if frame_number not in data1_list:
        missed_detection += 1

for frame_number in data1_list:
    if frame_number not in data2_list:
        false_alarm += 1

# 오차율 계산
total_count = 294
missed_detection_rate = (missed_detection / total_count) * 100
false_alarm_rate = (false_alarm / total_count) * 100

# 결과 출력
print("Missed Detection: ", missed_detection)
print("False Alarm: ", false_alarm)
print("Missed Detection Rate:", missed_detection_rate)
print("False Alarm Rate:", false_alarm_rate)
