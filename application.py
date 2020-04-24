from noticrawlpost import Crawler as cw
import json
import sys
import papers
from flask import Flask, request, jsonify
import most_similar

app = Flask(__name__)


def get_url(location):
    data = {"검암경서동": "gumam", "연희동": "yeonhi", "청라1동": "cheongna1", "청라3동": "cheongna3", "청라2동": "cheongna2", "가정1동": "gajeong1", "가정2동" :",gajeong2" , "가정3동" : "gajeong3", "신현원창동" : "sinhyun", "석남1동" :"seoknam1", "석남2동" : "seoknam2", "석남3동" : "seoknam3" , "가좌1동" :"gajwa1", "가좌2동" :"gajwa2" , "가좌3동" : "gajwa3" , "가좌4동" :"gajwa4", "검단동" :"gumdan1", "불로대곡동" :"gumdan2","원당동":"gumdan3", "당하동":"gumdan4","마전동":"majeon", "오류왕길동":"gumdan5"}
    if location in data:
        return data[location]
    else:
        return False
# 딱맞는 장소를 입력하지 않는다면, most_similar.py에 있는 most_similar_list 함수를 통해 가장 비슷한 것들 배열을 호출.
# 딱맞는 장소 입력시 리턴값 : str, 비슷한 장소 입력시 리턴값 : list
@app.route('/paper', methods=['POST'])
def paper():
    req = request.get_json()
    paper_cata = req["action"]["detailParams"]["paper"]["value"]
    paper_cata.replace(" ", "")
    # order_command = req["action"]["detailParams"]["command"]["value"]
    if papers.get_db_row(paper_cata) is not False:
        print(papers.get_db_row(paper_cata), sys.stderr)
    res = {
        "version": "2.0",
        "template": {
        "outputs": [
                {
                    "simpleText" : {
                        "text" : papers.get_db_row(paper_cata)
                    }
                }
            ]
        }
    }
    return jsonify(res)

# 유사도를 비교해서 유사 내용이 많다면 나온다면 재질문으로 버튼을 등록.
@app.route('/noti', methods=['POST'])
def noti():
    req = request.get_json()
    location = req["action"]["detailParams"]["sys_location"]["value"]
    command = req["action"]["detailParams"]["noti"]["value"]
    # TODO : command가 알려줘라면 noti로, 신청이라면 paper로
    if get_url(location) is False:
        url = "cheongna2"
    else:
        url = get_url(location)
    post = cw(url)
    titles = post.get_titles()
    links = post.get_links()
#     링크와 타이틀을 다 읽어옴
    length = len(links)
    res = {
        "version": "2.0",
        "template": {
        "outputs": [
            {
            "carousel": {
                "type": "basicCard",
                "items": [
                        ]
                    }
                }
            ]
        }
    }
    for index in range(length):
        b = {
                "title": location + "공지소식",
                    "description": titles[index],
                    "thumbnail":
                    {
                        "imageUrl": "http://www.seo.incheon.kr/open_content/main/images/contents/seogu/symbol01.gif"
                    },
                    "buttons": [
                    {
                        "action":  "webLink",
                        "label": "자세히",
                        "webLinkUrl": links[index]
                    }
                ]
            }
        res["template"]["outputs"][0]['carousel']['items'].append(dict(b))
    return jsonify(res)


if __name__ == "__main__":
    # noti()
    app.run(host='0.0.0.0', port=5000, threaded=True)
