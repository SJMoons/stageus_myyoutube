import pafy

url = 'https://youtu.be/vxnqh8KwxTs'
video_info = pafy.new(url)

print('TITLE : %s' % video_info.title)
print('RATING : %s' % video_info.rating)
print('VIEWCOUNT : %s' % video_info.viewcount)
print('AUTHOR : %s' % video_info.author)