class single_text:
    def __init__(self, text):
        text = str(text)
        self.res = {"version": "2.0", "template": {"outputs": [{"simpleText": {"text" : text}}], "quickReplies":[]}}

    def change_res(self, text):
        self.res["template"]["outputs"][0]["simpleText"]["text"] = str(text)

    def add_quick_btn(self, ele_list, block_id):
        for string in ele_list:
            ele = {"messageText": "대형폐기물 스티커", "action": "block", "label": string, "blockId": block_id}
            self.res["template"]["quickReplies"].append(ele)

    def get_res(self):
        return self.res
