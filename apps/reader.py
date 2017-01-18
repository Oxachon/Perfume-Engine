import json

def json_parser (filename):
    with open(filename) as data_file:
        return json.load(data_file)

