import json

def json_parser ():
    with open('system/json_example.json') as data_file:
        return json.load(data_file)

