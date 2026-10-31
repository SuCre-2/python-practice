#只管读写
import json

FILE = 'scores.json'

def load():
    try:
        with open(FILE,'r',encoding='utf-8')as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return[]

def save(records):
    with open(FILE,'w',encoding='utf-8')as f:
        json.dump(records,f,ensure_ascii=False,indent=2)