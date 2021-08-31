# Homebrew로 파이썬 설치하기

Homebrew를 사용하는 이유
- 설치 삭제가 용의하며 macos에 최적화 되어 있기 때문이다

Homebrew 설치후 which brew를 치면 설치 경로가 나타난다

brew install python3 - 파이썬 3 를 설치


# 셀레니움 유튜브 스크래핑

사이트 로딩이 다 안되면 그 전에 작업을 수행해 원하는 결과를 수행못할떄가 있다
그럴떈 아래 코드를 입력해 로딩이 될떄까지 동작을 기다릴수 있다 

-driver.implicitly_wait(10)

# 랄로 라는 채널의 영상 제목을 가져올것이다 일단 랄로 채널의 들어가야한다

search='랄로'
driver.get("https://www.youtube.com/results?search_query="+search)

# BeautifulSoup

req = driver.page_source                          
soup=BeautifulSoup(req, 'html.parser')            
                                                  
titleList = soup.find_all('a', id='video-title')  

html 코드 전체를 불러와 a 타입을 가진 video-title 전체를 가져온다

# 파일 출력

for title in titleList:     
    print(title['title'])   

for 문으로 title 전체를 불러온다

