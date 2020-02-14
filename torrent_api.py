import qbittorrentapi


def auth():
    qbt_client = qbittorrentapi.Client(host='localhost:8081', username='admin', password='admin123')

    try:
        qbt_client.auth_log_in()
        print(f'qBittorrent: {qbt_client.app.version}')
        print(f'qBittorrent Web API: {qbt_client.app.web_api_version}')
    except qbittorrentapi.LoginFailed as e:
        print(e)

    return qbt_client


def download(qbt_client, path, magnet):
    return qbt_client.torrents_add(urls=magnet, save_path=path)
