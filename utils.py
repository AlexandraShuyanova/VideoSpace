from flask import json


def read_config():
    with open('conf/api.json') as json_file:
        data = json.load(json_file)
        return data['downloadFolder'], data['serverAddress']
