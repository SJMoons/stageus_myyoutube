# import vlc
# from PyQt5 import QtCore, QtGui, QtWidgets
# import time
# import threading
# # media = vlc.MediaPlayer("News.mp4")
# # # media.play()
# import urllib.request
# from urllib import parse

# import requests

# input = "파이썬"
# params = {"search_query": input}
# querystring = parse.urlencode(params)
# print(querystring)

# parseResult = parse.urlparse("https://www.youtube.com/results" + "?" + querystring)
# print(parseResult)
# print(parseResult[4])
# # answer = "한글"
# # search = str(answer.encode("utf-8"))
# # print(search)

# url = "https://www.youtube.com/results" + "?" + querystring
# res = requests.get(url)
# # res.status_code       #200이 나오면 정상
# # print(res.status_code)
# # res.text
# # print(res.json())
# print(res.text)

# import pafy     #크롤링

# url = "https://www.youtube.com/results" + "?" + querystring
# try:
#     v = pafy.new(url)
# except KeyError:
#     pass
# title = v.title
# author = v.author
# viewCount = v.viewcount
# print(viewCount)
# print(title)
# print(author)


# self.videoframe = QFrame(self.ui.videoPlayPage)

# self.videoframe.setGeometry(QtCore.QRect(210, 70, 391, 291))

# self.videoframe.setFrameShape(QtWidgets.QFrame.Box)

# self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)

# self.vboxlayout = QVBoxLayout()

# )

# resp = urllib.request.urlopen(url)
# print(resp.read())
# resp.isclosed()
# resp.code
# html = resp.read().decode("utf-8")
# print(html[:500])



# import urllib.request
# import requests
# import pafy

# url = "https://youtu.be/vxnqh8KwxTs"
# req = requests.get(url)
# print(req.encoding)



# import pafy,vlc
# url="https://youtu.be/vxnqh8KwxTs"
# video=pafy.new(url)
# best = video.getbestaudio()
# playurl = best.url
# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(playurl)
# Media.get_mrl()
# player.set_media(Media)
# player.play()
# time.sleep(10)



# import time
# import vlc

# # if __name__ == "__main__":
# media = vlc.MediaPlayer("News.mp4")
# media.play()
# time.sleep(1000)



# importing time and vlc
# import vlc
 

# class Vlc(threading.Thread, QtCore.QObject):   #쓰레드 클래스가 두개 이상 클래스에 쓰이면 클래스를 만들고 하나에만 쓰이면 게임페이지에 한 파일로 만들기
#     resultSignal = QtCore.pyqtSignal(str)   # FEEDBACK: 쓰레드를 통한 결과값을 받는 방법 중 1개 ( Signal/Slot )
#                                             # FEEDBACK: 클래스 안에서 사용하는 전역변수 즉, 멤버변수와 동일하지만 이렇게 적어주어야만 함

#     def __init__(self, revui):
#         threading.Thread.__init__(self)
#         QtCore.QObject.__init__(self)
# # method to play video
#     def video(source):
        
#         # creating a vlc instance
#         vlc_instance = vlc.Instance()
        
#         # creating a media player
#         player = vlc_instance.media_player_new()
        
#         # creating a media
#         media = vlc_instance.media_new(source)
        
#         # setting media to the player
#         player.set_media(media)
        
#         # play the video
#         player.play()
        
#         # wait time
#         time.sleep(0.5)
        
#         # getting the duration of the video
#         duration = player.get_length()
        
#         # printing the duration of the video
#         print("Duration : " + str(duration))

#         # time.sleep(duration)
        
#     # call the video method
#         # video("News.mp4")

#     if __name__ == '__main__':
#         video("News.mp4")