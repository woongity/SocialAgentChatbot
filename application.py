from crawlpost import Crawler as cw
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/noti', methods=['POST'])
def noti():
    req = request.get_json()
    location = req["action"]["detailParams"]["sys_location"]["value"]
    command = req["action"]["detailParams"]["noti"]["value"]
    titles = cw
    
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": location + command + str(titles[0])
                    }
                }
            ]
        }
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
