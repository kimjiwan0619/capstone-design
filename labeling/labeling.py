import cv2
from time import sleep
import threading
import keyboard

# 동영상 이름
video_name = "video_test1" + ".mp4"

# 동영상 파일 경로
video_path = '../video_to_frame/video_forder/' + video_name

# result 파일 경로
txt_path = './result/' + video_name[:-4]

def split_video_into_frames(video_path):
    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)

    # set threading
    h = Hook()  # 훅 쓰레드 생성
    h.start()  # 쓰레드 실행

    # 프레임 카운터 초기화
    frame_counter = 1

    # 프레임 단위로 동영상 읽기
    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        # 비디오의 마지막 프레임에 도달하면 종료
        if not ret: break

        # 프레임 출력
        cv2.imshow('result', frame)
        if cv2.waitKey(1) == ord('q'): break
        if frame_counter == 0: input("Press any key to continue")

        # delay
        sleep(0.02)

        # 휴먼 레이블링 - thread 동작부
        # 키보드(d)를 누르면 알람 on / 키보드(s)를 누르면 알람 off
        if h.event == True:
            with open(txt_path + '_labeling.txt', 'a') as f:
                f.write(('%d ' + 'ON \n') % (frame_counter))
            print(('%d ' + 'ON') % (frame_counter))

        elif h.event == False:
            with open(txt_path + '_labeling.txt', 'a') as f:
                f.write(('%d ' + 'OFF \n') % (frame_counter))
            print(('%d ' + 'OFF') % (frame_counter))

        # 다음 프레임으로 넘어가기
        frame_counter += 1

    # 캡처 객체 해제
    cap.release()

    with open(txt_path + '_labeling.txt', 'a') as f:
        f.write('\n')


# 휴먼 레이블링 - thread 선언부
class Hook(threading.Thread):
    def __init__(self):
        super(Hook, self).__init__()  # parent class __init__ 실행
        self.daemon = True  # 데몬쓰레드로 설정
        self.event = False  # D, S가 눌리면 event 발생
        keyboard.unhook_all()  # 후킹 초기화
        keyboard.add_hotkey('d', print, args=['D was pressed'])  # D가 눌리면 print 실행
        keyboard.add_hotkey('s', print, args=['S was pressed'])  # S가 눌리면 print 실행

    def run(self):  # run method override
        print('Hooking Started')
        while True:
            key = keyboard.read_hotkey(suppress=False)  # hotkey를 계속 읽음
            if key == 'd':  # d 받은 경우
                self.event = True  # event 클래스 변수를 True로 설정
            elif key == 's':  # s 받은 경우
                self.event = False  # event 클래스 변수를 False로 설정


split_video_into_frames(video_path)