from noticrawlpost import Crawler as cw
from citynoticrawl import CityCrawler
import json
from flask import Flask, request, jsonify
import sys
import values_py
sys.path.append('/workspace/kakaobot/views')
from cardview import carousel_card
from simpletextview import single_text


app = Flask(__name__)


@app.route('/minwon', methods=['POST'])
def minwon():
    req = request.get_json()
    resource = req["action"]["detailParams"]["submit_complaints"]["value"]

@app.route('/trash',methods=['POST'])
def trash():
    req = request.get_json()
    # buying_place = req['action']['detailParams']['buying_place']['value']
    trash_cata = req['action']['detailParams']["trash_cata"]["value"]
    print(trash_cata)
    # print(buying_place)
    res = single_text(values_py.get_cata(trash_cata))
    response = res.get_res()
    return jsonify(response)

@app.route('/seoguNoti', methods=['POST'])
def seoguNoti():
    req = request.get_json()
    location = req["action"]["detailParams"]["location"]["value"]
    command = req["action"]["detailParams"]["order_command"]["value"]
    post = cw("https://www.seo.incheon.kr/open_content/main/community/news/notice.jsp")
    titles = post.get_titles()
    links = post.get_links()
    imageUrl = "http://www.traveli.co.kr/repository/area/logo/162.png"
    res = carousel_card()
    for index in range(0, 9):
        res.append_ele(location, titles[index], imageUrl, links[index])
    response = res.get_res()
    return jsonify(response)


@app.route('/icnNoti', methods=['POST'])
def icnNoti():
    req = request.get_json()
    cata = req["action"]["detailParams"]["order_command1"]["value"]
    command = req["action"]["detailParams"]["order_command"]["value"]
    location = req["action"]["detailParams"]["location"]["value"]
    board_cata = {"일반": "http://www.incheon.go.kr/IC010101", "행사": "http://www.incheon.go.kr/IC010501"}
    url = "http://www.incheon.go.kr/IC010101"
    print(cata)
    if cata in board_cata:
        url = board_cata[cata]
    post = CityCrawler(url)
    titles = post.get_titles()
    try:
        links = post.get_links()
    except TypeError:
        links = " "
    res = carousel_card()
    imageUrl = "http://www.traveli.co.kr/repository/area/logo/162.png"
    for index in range(1, 10):
        res.append_ele("인천시", titles[index], imageUrl, links)
    response = res.get_res()
    return jsonify(response)


# 유사도를 비교해서 유사 내용이 많다면 나온다면 재질문으로 버튼을 등록.
@app.route('/dongNoti', methods=['POST'])
def dongNoti():
    req = request.get_json()
    location = req["action"]["detailParams"]["location"]["value"]
    command = req["action"]["detailParams"]["order_command"]["value"]
    post = cw("http://www.seo.incheon.kr/open_content/dong/sub/dong_notice.jsp?dong="+dong.get_url(location))
    titles = post.get_titles()
    links = post.get_links()
#     링크와 타이틀을 다 읽어옴
    res = carousel_card()
    imageUrl = "http://www.traveli.co.kr/repository/area/logo/162.png"
    for index in range(0, 9):
        if values_py.get_url(location) == "cheongna2":
            location = "청라2동"
        res.append_ele(location, titles[index], imageUrl, links[index])
    response = res.get_res()
    return jsonify(response)


if __name__ == "__main__":
    # noti()
    app.run(host='0.0.0.0', port=5000, threaded=True)
