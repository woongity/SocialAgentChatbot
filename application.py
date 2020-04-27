from noticrawlpost import Crawler as cw
import json
from flask import Flask, request, jsonify

import sys
sys.path.append('/workspace/kakaobot/views')
from cardview import carousel_card
import simpletextview

app = Flask(__name__)


def get_url(location):
    data = {"검암경서동": "gumam", "연희동": "yeonhi", "청라1동": "cheongna1", "청라3동": "cheongna3", "청라2동": "cheongna2", "가정1동": "gajeong1", "가정2동" :",gajeong2" , "가정3동" : "gajeong3", "신현원창동" : "sinhyun", "석남1동" :"seoknam1", "석남2동" : "seoknam2", "석남3동" : "seoknam3" , "가좌1동" :"gajwa1", "가좌2동" :"gajwa2" , "가좌3동" : "gajwa3" , "가좌4동" :"gajwa4", "검단동" :"gumdan1", "불로대곡동" :"gumdan2","원당동":"gumdan3", "당하동":"gumdan4","마전동":"majeon", "오류왕길동":"gumdan5"}
    if location in data:
        return data[location]
    else :
        return "gumdan3"

# 딱맞는 장소를 입력하지 않는다면, most_similar.py에 있는 most_similar_list 함수를 통해 가장 비슷한 것들 배열을 호출.
# 딱맞는 장소 입력시 리턴값 : str, 비슷한 장소 입력시 리턴값 : list
@app.route('/paper', methods=['POST'])
def paper():
    req = request.get_json()
    paper_cata = req["action"]["detailParams"]["paper"]["value"]
    paper_cata.replace(" ", "")
#     모든 이름 문자열은 스페이스를 제거한다.
    order_command = req["action"]["detailParams"]["command"]["value"]
    print(order_command, file=sys.stderr)
    if papers.get_db_row(paper_cata) is not False:
        print(papers.get_db_row(paper_cata), sys.stderr)
    return jsonify(res)

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
    location = req["action"]["detailParams"]["sys_location"]["value"]
    command = req["action"]["detailParams"]["order_command"]["value"]
    # TODO : command가 알려줘라면 noti로, 신청이라면 paper로
    post = cw(get_url(location))
    titles = post.get_titles()
    links = post.get_links()
#     링크와 타이틀을 다 읽어옴
    res = carousel_card()
    imageUrl = "http://www.traveli.co.kr/repository/area/logo/162.png"
    for index in range(0,9):
        if get_url(location) == "gumdan3":
            location = "검단3동"
        res.append_ele(location,titles[index],imageUrl,links[index])  
    response = res.get_res()
    return jsonify(response)


if __name__ == "__main__":
    # noti()
    app.run(host='0.0.0.0', port=5000, threaded=True)
