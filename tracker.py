from pathlib import Path

from flask import Flask, jsonify
import os
from flask import request
from flask_cors import CORS
from flask import json
from flask import abort
import torrent_api
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "Hi!!!"


@app.route('/files/', methods=['POST'])
def passage():
    if not request.is_json:
        abort(400)
    file_name = request.get_json(silent=True)
    if file_name is None:
        return json.dumps({'message': 'fuck you!'}), 200, {'ContentType': 'application/json'}
    if 'film' in file_name:
        new_file_name = file_name['film']
    else:
        return json.dumps({'message': 'Error!'}), 200, {'ContentType': 'application/json'}
    folder = 'C:/webServer/torrents'
    for element in os.scandir(folder):
        if element.is_file():
            if element.name.startswith(new_file_name):
                return json.dumps({'message': folder + '/' + element.name}), 200, {'ContentType': 'application/json'}
    return json.dumps({'message': 'Sorry, file is not found..('}), 200, {'ContentType': 'application/json'}


@app.route('/download/', methods=['POST'])
def download():
    if not request.is_json:
        abort(400)

    data = request.get_json()

    if 'magnet' not in data:
        abort(400)

    result = torrent_api.download(torrent_api.auth(), data['magnet'])

    if result == 'Ok.':
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return json.dumps({'success': False}), 304, {'ContentType': 'application/json'}


@app.route('/library/', methods=['GET'])
def all_files():
    films_list = []
    i = 0
    folder = 'C:/webServer/torrents'
    for element in os.scandir(folder):
        if element.is_file():
            path = folder + '/' + element.name
            film_info = {'id': i, 'name': element.name, 'path': path, 'type': Path(path).suffix}
            films_list.append(film_info)
            i += 1
    print(films_list)
    return json.dumps({'films': films_list}, ensure_ascii=False), 200, {'ContentType': 'application/json'}









if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')