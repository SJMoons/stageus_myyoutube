# import pafy

# url = 'https://youtu.be/vxnqh8KwxTs'
# video_info = pafy.new(url)

# print('TITLE : %s' % video_info.title)
# print('RATING : %s' % video_info.rating)
# print('VIEWCOUNT : %s' % video_info.viewcount)
# print('AUTHOR : %s' % video_info.author)

# import vlc
 
 
# class VlcPlayer:
#     '''
#     args: VLC인스턴스 생성옵션
#     '''
    
#     def __init__(self, *args):
#         if args:
#             instance = vlc.Instance(*args)
#             self.media = instance.media_player_new()
#         else:
#             self.media = vlc.MediaPlayer()
 
#     def set_uri(self, mrl):
#         '''
#         스트리밍 url주소 또는 로컬 재생파일을 설정
#         :param mrl: 스트리밍주소
#         :return:
#         '''
#         self.media.set_mrl(mrl)
 
#     def play(self, path=None):
#         '''
#         미디어 재생
#         :param path:
#         :return: 성공:0, 실패:-1
#         '''
#         if path:
#             self.set_uri(path)
#             return self.media.play()
#         else:
#             return self.media.play()
 
#     def pause(self):
#         '''
#         재생 멈춤
#         :return:
#         '''
#         self.media.pause()
 
#     def resume(self):
#         '''
#         재생 다시 시작
#         :return:
#         '''
#         self.media.set_pause(0)
 
#     def stop(self):
#         '''
#         재생 멈춤
#         :return:
#         '''
#         self.media.stop()
 
#     def release(self):
#         '''
#         미디어 소스 초기화
#         :return:
#         '''
#         return self.media.release()
 
#     def is_playing(self):
#         '''
#         플레이 상태 확인
#         :return: 재생중 : 1, 재생중이지 않음 : 0
#         '''
#         return self.media.is_playing()
 
#     def get_time(self):
#         '''
#         Elapsed time, return millisecond value
#         :return:
#         '''
#         return self.media.get_time()
 
#     def set_time(self, ms):
#         '''
#         미디어 특정시간으로 이동.
#         :param ms:
#         :return: 성공 : 0, 실패 : -1
#         '''
#         return self.media.get_time(ms)
 
#     # The total length of audio and video, returns the value in milliseconds
#     def get_length(self):
#         '''
#         미디어소스의 재생길이
#         :return: 재생길이(ms)
#         '''
#         return self.media.get_length()
 
#     def get_volume(self):
#         '''
#         :return: 현재 볼륨 상태 값 (0~100)
#         '''
#         return self.media.audio_get_volume()
 
#     def set_volume(self, volume):
#         '''
#         볼륨 설정
#         :param volume: 0~100 사이 값
#         :return:
#         '''
#         return self.media.audio_set_volume(volume)
 
#     # Return to the current state: playing; paused; other
#     def get_state(self):
#         '''
#         현재 플레이어 상태 확인
#         :return: playing : 1, paused : 0, 그외 -1
#         '''
#         state = self.media.get_state()
#         if state == vlc.State.Playing:
#             return 1
#         elif state == vlc.State.Paused:
#             return 0
#         else:
#             return -1
 
#     def get_position(self):
#         '''
#         현재 playback 진척도
#         :return: 미디어의 재생율 (1 이하 소숫점)
#         '''
#         return self.media.get_position()
 
#     def set_position(self, float_val):
#         '''
#         특정 재생율로 미디어의 재생위치를 변경.
#         :param float_val: 0~1 사이 float값
#         :return:
#         '''
#         return self.media.set_position(float_val)
 
#     def get_rate(self):
#         '''
#         :return: 재생속도
#         '''
#         return self.media.get_rate()
 
#     def set_rate(self, rate):
#         '''
#         재생속도 설정
#         :param rate: 배속
#         :return:
#         '''
#         return self.media.set_rate(rate)
 
#     def set_ratio(self, ratio):
#         '''
#         Set the aspect ratio (such as "16:9", "4:3")
#         :param ratio:
#         :return:
#         '''
#         # Must be set to 0, otherwise the screen width and height cannot be modified
#         self.media.video_set_scale(0) 
#         self.media.video_set_aspect_ratio(ratio)
 
#     def add_callback(self, event_type, callback):
#         '''
#         콜백 listener 설정
#         :param event_type: vlc listener 환경변수
#         :param callback: 콜백함수
#         :return:
#         '''
#         self.media.event_manager().event_attach(event_type, callback)
 
#     def remove_callback(self, event_type, callback):
#         '''
#         Remove listener
#         :param event_type:
#         :param callback:
#         :return:
#         '''
#         self.media.event_manager().event_detach(event_type, callback)

#     def my_call_back(event):
#         print("콜백함수호출: 종료호출")
#         global status 
#         status = 1 
 
# if "__main__" == __name__:
 
#     # 뮤직비디오 파일
#     media_file = "News.mp4"
 
#     player = VlcPlayer()
#     player.add_callback(vlc.EventType.MediaPlayerStopped,vlc.callbackmethod)
 
#     player.play(media_file)
#     # player.set_position() #테스트를 위해 영상의 90%위치로 이동시킵니다.
#     player.set_rate(1) # 재생속도를 2배속으로 설정합니다.
 
#     status = 0
#     while True:
#         if status == 1:
#             break
#         else:
#             pass

# importing vlc module
# import vlc
# import time
# # # importing pafy module
# import pafy
  
# # url of the video
# url = "https://www.youtube.com/watch?v=gUyCa6errBc"

# video = pafy.new(url)
# best = video.getbest()
# playurl = best.url
# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(playurl)
# Media.get_mrl()
# player.set_media(Media)
# player.play()

# time.sleep(120)

import sys

import os.path

from PyQt5.QtCore import Qt, QTimer

from PyQt5.QtGui import QPalette, QColor

from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QSlider, QHBoxLayout, QPushButton, \
    QVBoxLayout, QAction, QFileDialog, QApplication

import vlc

from PyQt5 import QtCore, QtGui, QtWidgets

class Player(QMainWindow):


    def __init__(self, master=None):

        QMainWindow.__init__(self, master)

        self.setWindowTitle("Media Player")

        # creating a basic vlc instance

        self.instance = vlc.Instance()

        # creating an empty vlc media player

        self.mediaplayer = self.instance.media_player_new()

        self.isPaused = False



         ##########video frame

        self.videoframe = QFrame(self)

        self.videoframe.setGeometry(QtCore.QRect(210, 70, 391, 291))

        self.videoframe.setFrameShape(QtWidgets.QFrame.Box)

        self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)

        self.vboxlayout = QVBoxLayout()

        self.vboxlayout.addWidget(self.videoframe)




        ######### the vlc

        self.filename='C:/Users/Kikomi/Pictures/Camera Roll/kk.mp4'

        self.media = self.instance.media_new(self.filename)

        self.mediaplayer.set_media(self.media)

        self.mediaplayer.play()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    player = Player()

    player.show()

    player.resize(640, 480)

    if sys.argv[1:]:

        player.OpenFile(sys.argv[1])

    sys.exit(app.exec_())




# video = pafy.new(url)
#             best = video.getbest()
#             playurl = best.url
#             Instance = vlc.Instance()
#             player = Instance.media_player_new()x
#             Media = Instance.media_new(playurl)
#             Media.get_mrl()
#             player.set_media(Media)x
#             player.play()x

# self.vlc_instance = vlc.Instance()
# self.mediaplayer = self.vlc_instance.media_player_new()
# self.mediaplayer.set_hwnd(int(self.frame.winId()))
# self.media_path = "test_video.mp4"
# self.media = self.vlc_instance.media_new(self.media_path)
# self.media.get_mrl()
# self.mediaplayer.set_media(self.media)
# self.mediaplayer.play() 


# creating pafy object of the video
# video = pafy.new(url)
  
# # getting best stream
# best = video.getbest()
  
# # creating vlc media player object
# media = vlc.MediaPlayer(best.url)
  
# # start playing video
# media.play()

# import pafy     #파이썬-vlc
 
# url = "https://www.youtube.com/watch?v=oYhOWagP_-E"
# video = pafy.new(url)

# print("video title : {}".format(video.title))  # 제목
# print("video rating : {}".format(video.rating))  # 평점
# print("video viewcount : {}".format(video.viewcount))  # 조회수
# print("video author : {}".format(video.author))  # 저작권자
# print("video length : {}".format(video.length))  # 길이
# print("video duration : {}".format(video.duration))  # 길이
# print("video likes : {}".format(video.likes)) # 좋아요
# print("video dislikes : {}".format(video.dislikes)) #싫어요

# best = video.getbest(preftype="mp4")
# print("best resolution : {}".format(best.resolution))

# cap = cv2.VideoCapture(best.url) 
 
# # 동영상 크기(frame정보)를 읽어옴
# frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
# # 동영상 프레임을 캡쳐
# frameRate = int(cap.get(cv2.CAP_PROP_FPS))
 
# frame_size = (frameWidth, frameHeight)
# print('frame_size={}'.format(frame_size))
# print('fps={}'.format(frameRate))
 
# # cv2.VideoWriter_fourcc(*'코덱')
# # codec 및 녹화 관련 설정
# # 인코딩 방식을 설정
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# #fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# #fourcc = cv2.VideoWriter_fourcc(*'MPEG')
# #fourcc = cv2.VideoWriter_fourcc(*'X264')
 
# out1Path = 'data/recode1.mp4'
# out2Path = 'data/recode2.mp4'
 
# # 영상 저장하기
# # out1Path : 저장할 파일명
# # fourcc : frame 압축 관련 설정(인코딩, 코덱 등)
# # frameRate : 초당 저장할 frame
# # frame_size : frame 사이즈(가로, 세로)
# # isColor : 컬러 저장 여부
# out1 = cv2.VideoWriter(out1Path, fourcc, frameRate, frame_size)
# out2 = cv2.VideoWriter(out2Path, fourcc, frameRate, frame_size)

# while True:
#     # 한 장의 이미지를 가져오기
#     # 이미지 -> frame
#     # 정상적으로 읽어왔는지 -> retval
#     retval, frame = cap.read()
#     if not(retval):
#         break  # 프레임정보를 정상적으로 읽지 못하면 while문을 빠져나가기
    
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# 회색으로 컬러 변환
#     edges = cv2.Canny(gray, 100, 200)	# Canny함수로 엣지 따기
    
#     # 동영상 파일에 쓰기
#     out1.write(frame)
#     out2.write(edges)
    
#     # 모니터에 출력
#     cv2.imshow('frame', frame)
#     cv2.imshow('edges', edges)
    
#     key = cv2.waitKey(frameRate)  # frameRate msec동안 한 프레임을 보여준다
    
#     # 키 입력을 받으면 키값을 key로 저장 -> esc == 27
#     if key == 27:
#         break
        
# if cap.isOpened():
#     cap.release()
#     out1.release()
#     out2.release()
    
# cv2.destroyAllWindows()