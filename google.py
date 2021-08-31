from selenium import webdriver
from bs4 import BeautifulSoup



driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(10)

search=''

driver.get("https://www.youtube.com/results?search_query="+search)
driver.find_element_by_id('avatar').click()
driver.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div').click()


req = driver.page_source
soup=BeautifulSoup(req, 'html.parser')

titleList = soup.find_all('a', id='video-title')

for title in titleList:
    print(title['title'])


