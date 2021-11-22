# 네이버 사이트의 모든 정보를 다 가져옴
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")
print(bsObject)



# 네이버 사이트의 제목을 가져옴 (head.title 사용)
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")
print(bsObject.head.title)

# 네이버 사이트의 메타 데이터를 가져옴(메타데이터 : 다른 데이터를 설명해주는 데이터)
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))



# find를 사용하면 원하는 태그의 정보만 얻어올 수 있다
# ex)네이버의 메타데이터를 가져오는 경우
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject.head.find("meta",{"name":"description"}).get('content'))

# 모든 링크의 텍스트와 주소 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.youtube.com")
bsObject = BeautifulSoup(html, "html.parser")
for link in bsObject.find_all('a'):
    print(link.text.strip(),link.get('href'))


# 네이버 사이트의 메타 데이터를 가져옴(메타데이터 : 다른 데이터를 설명해주는 데이터)
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791191438406")
bsObject = BeautifulSoup(html, "html.parser")
print(bsObject)


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.youtube.com/watch?v=Aev3mSMAtUQ&list=RDAev3mSMAtUQ&start_radio=1")
bsObject = BeautifulSoup(html, "html.parser")
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788959897001")
bsObject = BeautifulSoup(html, "html.parser")
print(bsObject)


# # # # # 교보문고 베스트셀러 책이름/저자/가격 정보를 불러오기 
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79")
bsObject = BeautifulSoup(html, "html.parser")

book_page_urls = []
for cover in bsObject.find_all('div',{'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)
print(book_page_urls)

for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html,"html.parser")
    title = bsObject.find('meta',{'property':'og:title'}.get('content'))
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta',{'property':'image'}.get('content'))
    url = bsObject.find('meta',{'property':'url'}.get('content'))
    price = bsObject.find('meta',{'property':'price'}.get('content'))

    print(index+1,"\n" + "제목 :"+str(title),"\n" + "저자 :" + str(author), "\n" + "이미지 : "+str(image),"\n" + "링크 : " + str(url),"\n" + "가격 : " + str(price))
# print(bsObject.head.find("meta",{"name":"description"}).get('content'))



from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788959897001")
bsObject = BeautifulSoup(html, "html.parser")
print(bsObject.head.find("meta",{"property":"og:title"}).get('content'))

book_page_urls = []

for cover in bsObject.find_all('div',{'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)
print(book_page_urls)

for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html,"html.parser")
    title = bsObject.find('meta',{'property':'og:title'}.get('content'))
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta',{'property':'image'}.get('content'))
    url = bsObject.find('meta',{'property':'url'}.get('content'))
    price = bsObject.find('meta',{'property':'price'}.get('content'))

    print(index+1,"\n" + "제목 :"+str(title),"\n" + "저자 :" + str(author), "\n" + "이미지 : "+str(image),"\n" + "링크 : " + str(url),"\n" + "가격 : " + str(price))
# print(bsObject.head.find("meta",{"name":"description"}).get('content'))


