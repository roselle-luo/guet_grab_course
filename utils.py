import json


def json_perfect_out(text):
    print(json.dumps(text, indent=4, ensure_ascii=False))