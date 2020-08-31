import bs4 as bs
import urllib.request

sauce=urllib.request.urlopen("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv").read()
soup = bs.BeautifulSoup(sauce,'lxml')
num=1
for title in soup.find_all('td', class_="titleColumn"):
    
    name=title.find('a')
    print(str(num)+'.'+name.text)
    num += 1
