from bs4 import BeautifulSoup
import requests
import sqlite3
import os
import re 


def save_db_table(paper, cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS PAPERS(NAME TEXT, FACILITY TEXT, MANAGEMENT_FACILITY TEXT, CERTI TEXT, URL TEXT)''')
    cur.execute('INSERT INTO PAPERS VALUES (?,?,?,?,?)', (paper.get_name(), paper.get_facility(), paper.get_management_facility(), paper.get_cert(), paper.get_url()))


def append_sql(papers):
    try:
        conn = sqlite3.connect("/workspace/kakaobot/papers.db")
        cur = conn.cursor()
        for paper in papers:
            save_db_table(paper, cur)
            conn.commit()
    finally:
        conn.close()


def get_paperlist():
    paper_list = []
    for page in range(0, 554):
        url = "http://www.minwon.go.kr/main?a=AA170MinwonInfoListApp&sortStr=&deptIncCD=0&identity=&procIncCD=&online_yn=&cappKindCD=&CappBizSect=&vsect_inc_cd=&currentPage="+str(page)
        req = requests.get(url)
        html = req.content
        soup = BeautifulSoup(html, 'html.parser')
        f=open("addr.csv","w")
        com_te = ""
        for apost in range(1, 10):
            post = "#article > table > tbody > tr:nth-child("+str(apost)+") " + "> td:nth-child("
            link = "#article > table > tbody > tr:nth-child("+str(apost)+") > td.tl > " + "a:nth-child"
            paper = Papers(soup.select(post + "2)")[0].text.strip(), soup.select(post +"3)")[0].text.strip(), soup.select(post+"4)")[0].text.strip(), soup.select(post +"5)")[0].text.strip(), "http://www.minwon.go.kr"+soup.select(link+"(1)")[0].get("href"))
            print(paper.get_name(), paper.get_facility(), paper.get_management_facility(), paper.get_cert(), paper.get_url())
            com_te = com_te + paper.get_name()+',' +paper.get_facility()+',' + paper.get_management_facility()+',' + paper.get_cert()+',' + paper.get_url()
            com_te+='\n'
            paper_list.append(paper)
    f.write(com_te)
    f.close
    return paper_list
    # 서류 종류와 발급 기관, 관리 기관, 인증서 유무를 가지는 리스트를 리턴한다.


class Papers:
    def __init__(self, name, facility, management_facility, cert, url):
        self.name = name.replace(" ",'')
        self.facility = facility.replace(" ",'')
        self.management_facility = management_facility.replace(" ",'')
        self.cert = cert.replace(" ",'')
        self.url = url
        self.delete_data_in_bracket_name()

    def delete_data_in_bracket_name(self):
        name = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", self.name).replace('()', "").replace('[]', "")

        self.name = name

    def get_url(self):
        return self.url

    def get_name(self):
        return self.name

    def get_facility(self):
        return self.facility

    def get_management_facility(self):
        return self.management_facility

    def get_cert(self):
        return self.cert


if __name__ == "__main__":
    datas = get_paperlist()
    append_sql(datas)
