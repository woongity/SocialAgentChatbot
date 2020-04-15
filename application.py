from crawlpost import Crawler as cw
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/noti', methods=['POST'])
def noti():
    req = request.get_json()
    location = req["action"]["detailParams"]["sys_location"]["value"]
    command = req["action"]["detailParams"]["noti"]["value"]
    
    post = cw()
    titles = post.get_titles()
    links = post.get_links()
    
    res = {
        "version": "2.0",
        "template": {
        "outputs": [
        {
            "basicCard": {
            "title": "청라동소식",
            "description": str(titles[-1]),
            "thumbnail": {
            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
        },
        "profile": {
            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
            "nickname": "보물상자"
          },
          "buttons": [
            {
              "action":  "webLink",
              "label": "구경하기",
              "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
            }
          ]
        }
      }
    ]
  }
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
