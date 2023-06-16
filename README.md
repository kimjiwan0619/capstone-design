# capstone-design

## About The Project
* 좁은 골목길 사각지대 자동차 detection을 통한 사고 예방 프로젝트

## Built With
* YOLOv8
* Opencv

## Installation

1. Clone the repo
   ```
   git clone https://github.com/kimjiwan0619/capstone-design.git
   ```
2. Install packages 
   ```
   pip install requirements txt
   ```

## Usage

* 터미널 Command List <br>
**python track.py --source "n"** : 프로젝트 시작 및 웹캠 번호 "n" 설정.  <br>
**python track.py --source "path"** : 프로젝트 시작 및 녹화영상 경로 "path" 설정.  <br>
**--tracking-method bytetrack "deepocsort/botsort/strongsort/ocsort/bytetrack"** : tracking 알고리즘을 "deepocsort/botsort/strongsort/ocsort/bytetrack" 중 하나로 설정.  <br>
**--save-txt** : 녹화영상의 경우 프로젝트 결과를 text 파일로 저장. <br>
**--show-vid** : 녹화영상의 경우 런타임 도중 detection 과정을 영상으로 확인. <br>
**--tracking-direction "right/left"** : tracking 방향을 "right/left" 중 하나로 설정. <br> <br>
 
* 사용 예시  
   ```
   python track.py --source 0 --tracking-method bytetrack --tracking-direction right
   python track.py --source ../video_to_frame/video_forder/video_test9.mp4 --tracking-method bytetrack --save-txt --show-vid --tracking-direction right
   ``` 

## Contributing

프로젝트에 기여하고 싶으신 분들은 아래 절차를 따라주시기 바랍니다.  

1. 프로젝트 fork
2. feature branch 생성 (git checkout -b feature/name)
3. commit (git commit -m "Add feature")
4. push (git push origin feature/name)
5. pull request 생성

## License
yolov8_tracking 폴더의 LICENSE를 통해 라이센스 정보를 확인하세요.

## Contact

* 김지완: kimjiwan0619@khu.ac.kr
* 박건희: wm5256@naver.com  

* Project Link: git clone https://github.com/kimjiwan0619/capstone-design.git