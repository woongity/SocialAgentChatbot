from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        URL = "http://www.seo.incheon.kr/open_content/dong/sub/dong_notice.jsp?dong=cheongna2"
        req = Request(URL)
        page = urlopen(req)
        html = page.read()
        soup = BeautifulSoup(html, 'html.parser')
        self.posts = soup.select("#detail_con > div.board_list > table > tbody > tr > td.left.title > a")

    def get_titles(self):
        titles = []
        for post in self.posts:
            titles.append(post.text)
        return titles

    def get_links(self):
        links = []
        for post in self.posts:
            links.append("http://www.seo.incheon.kr"+post.get('href'))
        return links
