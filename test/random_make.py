import random

# 파일 생성 및 쓰기 모드로 열기
file = open("output.txt", "w")

# 1부터 100까지 출력하여 파일에 저장
for number in range(6, 200):
    number2 = random.choice([1, 2, 3])
    line = f"{number} {number2}"  # "number number2" 형식으로 줄 생성
    if number != 199:
        line += "\n"  # 마지막 줄을 제외한 줄에는 개행 추가
    file.write(line)

# 파일 닫기
file.close()