class carousel_card:
    def __init__(self):
        self.res = {"version": "2.0", "template": {"outputs": [{"carousel": {"type": "basicCard","items": []}}],"quickReplies":[]}}

    def append_ele(self, title, description, imageUrl, btnUrl):
        b = {"title": title, "description": description, "thumbnail": {"imageUrl": imageUrl}, "buttons": [{"action": "webLink", "label": "더보기", "webLinkUrl": btnUrl}]}
        self.res["template"]["outputs"][0]['carousel']['items'].append(b)

    def get_res(self):
        return self.res