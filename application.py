from noticrawlpost import Crawler as cw
import json
from flask import Flask, request, jsonify
import dong
import sys
sys.path.append('/workspace/kakaobot/views')
from cardview import carousel_card
import simpletextview

app = Flask(__name__)

@app.route('/minwon',methods=['POST'])
def minwon():
    

@app.route('/seoguNoti',methods=['POST'])
def seoguNoti():
    req = request.get_json()
    location = req["action"]["detailParams"]["location"]["value"]
    command = req["action"]["detailParams"]["order_command"]["value"]
    post = cw("https://www.seo.incheon.kr/open_content/main/community/news/notice.jsp")
    titles = post.get_titles()
    links = post.get_links()
    imageUrl = "http://www.traveli.co.kr/repository/area/logo/162.png"
    res = carousel_card()
    for index in range(0,9):
        res.append_ele(location,titles[index],imageUrl,links[index])  
    response = res.get_res()
    return jsonify(response)
    
    
# 유사도를 비교해서 유사 내용이 많다면 나온다면 재질문으로 버튼을 등록.
@app.route('/dongNoti', methods=['POST'])
def dongNoti():
    req = request.get_json()
    location = req["action"]["detailParams"]["location"]["value"]
    command = req["action"]["detailParams"]["order_command"]["value"]
    print(location,file=sys.stderr)
    # TODO : command가 알려줘라면 noti로, 신청이라면 paper로
    post = cw("http://www.seo.incheon.kr/open_content/dong/sub/dong_notice.jsp?dong="+dong.get_url(location))
    titles = post.get_titles()
    links = post.get_links()
#     링크와 타이틀을 다 읽어옴
    res = carousel_card()`
    imageUrl = "http://www.traveli.co.kr/repository/area/logo/162.png"
    for index in range(0,9):
        if dong.get_url(location) == "gumdan3":
            location = "검단3동"
        res.append_ele(location,titles[index],imageUrl,links[index])  
    response = res.get_res()
    return jsonify(response)


if __name__ == "__main__":
    # noti()
    app.run(host='0.0.0.0', port=5000, threaded=True)
