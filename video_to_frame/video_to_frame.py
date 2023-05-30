import cv2

# 동영상 이름
video_name = "video_test1" + ".mp4"

# 동영상 파일 경로
video_path = './video_forder/' + video_name

# 프레임을 저장할 디렉토리 경로
output_directory = './frames/'

def split_video_into_frames(video_path, output_directory, num_frames):
    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)
    
    # 프레임 카운터 초기화
    frame_counter = 0
    
    # 프레임 단위로 동영상 읽기
    while cap.isOpened() and frame_counter < num_frames:
        # 프레임 읽기
        ret, frame = cap.read()
        
        # 비디오의 마지막 프레임에 도달하면 종료
        if not ret:
            break
        
        # 프레임 저장 경로
        frame_path = output_directory + 'frame_{:04d}.jpg'.format(frame_counter)
        print(frame_path)
        
        # 프레임 저장
        cv2.imwrite(frame_path, frame)
        
        # 다음 프레임으로 넘어가기
        frame_counter += 1
    
    # 캡처 객체 해제
    cap.release()
    cv2.destroyAllWindows()
    
split_video_into_frames(video_path, output_directory, num_frames=200)

