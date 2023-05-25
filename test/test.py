# 1번째 텍스트 파일 읽기
file1 = open("/data/kimjiwan0619/capstone-design/yolov8_tracking/runs/track/exp2/tracks/frames.txt", "r")
data1 = file1.readlines()
file1.close()

# 2번째 텍스트 파일 읽기
file2 = open("output.txt", "r")
data2 = file2.readlines()
file2.close()

# 오차 계산을 위한 변수 초기화
missed_detection = 0
false_alarm = 0

file1_dict = {}
file2_dict = {}

for line in data1:
    frame_number, id, average_distance = line.strip().split()
    if frame_number not in file1_dict:
        file1_dict[frame_number] = set()
    file1_dict[frame_number].add(id)

for line in data2:
    frame_number, id = line.strip().split()
    if frame_number not in file2_dict:
        file2_dict[frame_number] = set()
    file2_dict[frame_number].add(id)

# 오차 계산
for frame_number in file2_dict:
    if frame_number not in file1_dict:
        missed_detection += len(file2_dict[frame_number])
    else:
        for id in file2_dict[frame_number]:
            if id not in file1_dict[frame_number]:
                missed_detection += 1

for frame_number in file1_dict:
    if frame_number not in file2_dict:
        false_alarm += len(file1_dict[frame_number])
    else:
        for id in file1_dict[frame_number]:
            if id not in file2_dict[frame_number]:
                false_alarm += 1

# 오차율 계산
total_count = len(data2)
missed_detection_rate = (missed_detection / total_count) * 100
false_alarm_rate = (false_alarm / total_count) * 100

# 결과 출력
print("Missed Detection Rate:", missed_detection_rate)
print("False Alarm Rate:", false_alarm_rate)
