#爬取小说2019.2.8，第一次写的爬取小说代码


import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLtext(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def getDATA(txt_first , html):
    soup = BeautifulSoup(html , "lxml")
    txtname = soup.find('h3',attrs={'class':'j_chapterName'})
    txtcontent = soup.find('div',attrs={'class':'read-content j_readContent'})
    for p in txtcontent:
        lines = p.string
        txt_first = txt_first + lines
    txt_first = txt_first.replace('　　','\n')
    return txt_first
    # print(txt_first)
    # txtcontent = txtcontent.replace("S","123")
    # for lines in txtcontent:
    #     txt_first = txt_first + lines
    # print(txt_first)

def savaDATA(txt_first,html):
    PATH = 'H:\\'
    f = open(PATH + "杨鑫爬取的第一篇小说.txt" , "w")
    f.write(txt_first)
    f.close()

def main():
    txt = ""
    url = 'https://www.readnovel.com/chapter/11118323003835503/29905715874512260'
    html = getHTMLtext(url)
    txt = getDATA(txt,html)
    savaDATA(txt,html)
    # print(txt)

main()