from urllib.request import urlopen
from urllib.parse import quote
from urllib.request import urlretrieve

# '개' 검색결과 받기
keyword = "개"
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" + quote(keyword)

result = urlopen(url)
print(result)

result_html = result.read()

# 개에 대한 태그 정보 찾기
from bs4 import BeautifulSoup

result_soup = BeautifulSoup(result_html,'html.parser')


img_tag = result_soup.find_all("img")
type(img_tag)

image_url = img_tag[4]["data-source"]

# 개 이미지 파일 다운로드
from urllib.request import urlretrieve

urlretrieve(image_url, './result/dog.jpg')

for i in range(4,54):
    try:
        image_url = img_tag[i]["data-source"]
        urlretrieve(image_url, './result/dog_{}.jpg'.format(i))
    except Exception as e:
        print(i, end=", ")
        print(e)

