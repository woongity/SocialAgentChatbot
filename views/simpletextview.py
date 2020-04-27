class single_text:
    def __init__(self,text):
        res = {"version": "2.0","template": {"outputs": [{"simpleText" : {"text" : text}}]}}
        
    def change_res(self,text):
        self.res["template"]["outputs"][0]["simpleText"]["text"]=text
        
    def get_res(self):
        return self.res