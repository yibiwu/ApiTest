import json


class JsonUtil():
    def write_json(self,data):
        with open("../data/json/request.json", "w") as f:
            json.dump(data, f)
        print("加载入文件完成...")

    def read_json(self):
        with open("../data/json/request.json", "r") as f:
            json.load(f)
        print("文件打开完成...")
