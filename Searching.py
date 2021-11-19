import pafy
url = input("Enter the complete URL of the Video")

video = pafy.new(url)

streams = video.streams

for i in streams:
    print(i)



best = video.getbest()


print(best)

best.download()

print("Video downloaded successfully")