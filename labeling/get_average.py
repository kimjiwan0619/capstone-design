# 동영상 이름
video_name = "video_test1" + "_labeling.txt"

# result 파일 경로
txt_path = './result/' + video_name[:-4]

# 레이블링 횟수 (분모)
num = 3

# 1번째 텍스트 파일 읽기
file1 = open(txt_path + ".txt", "r")
data1 = file1.readlines()
file1.close()

file1_dict = {}

for line in data1:
    if line != "\n":
        frame_number, on_off = line.strip().split()
        if frame_number not in file1_dict:
            file1_dict[frame_number] = list()

        if on_off == "ON":
            file1_dict[frame_number].append(1)
        elif on_off == "OFF":
            file1_dict[frame_number].append(0)

for frame_number in file1_dict:
    with open(txt_path + '_average.txt', 'a') as f:
        if round(sum(file1_dict[frame_number]) / num) == 1:
            f.write(('%s ' + 'ON \n') % (frame_number))
        elif round(sum(file1_dict[frame_number]) / num) == 0:
            f.write(('%s ' + 'OFF \n') % (frame_number))