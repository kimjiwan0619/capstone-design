# 1번째 텍스트 파일 읽기
file1 = open("/data/kimjiwan0619/capstone-design/yolov8_tracking/runs/track/exp2/tracks/frames.txt", "r")
data1 = file1.readlines()
file1.close()

# 2번째 텍스트 파일 읽기
file2 = open("output.txt", "r")
data2 = file2.readlines()
file2.close()

# 오차 계산을 위한 변수 초기화
error_count = 0
total_count = len(data2)

# 2번째 텍스트 파일 데이터 확인
for line in data2:
    frame_number, id = line.strip().split()  # 공백을 기준으로 데이터 분리
    frame_number = int(frame_number)
    id = int(id)
    
    # 1번째 텍스트 파일과 비교
    found = False
    for line2 in data1:
        frame_number2, id2, average_distance = line2.strip().split()  # 공백을 기준으로 데이터 분리
        frame_number2 = int(frame_number2)
        id2 = int(id2)
        
        if frame_number == frame_number2 and id == id2:
            found = True
            break
    
    # 비교 결과에 따라 오차 계산
    if not found:
        error_count += 1

# 오차율 계산
error_rate = (error_count / total_count) * 100

# 결과 출력
print("오차율:", error_rate)
