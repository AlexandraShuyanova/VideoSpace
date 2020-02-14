window.onload = function() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/library/', false);
    xhr.send();
    if(xhr.status !== 200) {
        alert('Ошибка соединения с сервером');
    }

    const data = JSON.parse(xhr.responseText);

    for(let i = 0;i<data.films.length;i++){
        let film_class = document.createElement('div');
        film_class.className = 'film';
        let video = document.createElement('video');
        video.controls='controls';
        video.width = '400';
        video.height = '300';

        let source_1 = document.createElement('source');
        source_1.src = data.films[i].path;
        source_1.type = 'video/mp4;codecs="avc1.42E01E, mp4a.40.2"';

        let source_2 = document.createElement('source');
        source_2.src = data.films[i].path;
        source_2.type = 'video/webm;codecs="vp8, vorbis"';

        let source_3 = document.createElement('source');
        source_3.src = data.films[i].path;
        source_3.type = 'video/ogg; codecs="theora, vorbis"';

        video.append(source_1);
        video.append(source_2);
        video.append(source_3);

        film_class.append(video);
        let library = document.getElementById('library_id');
        library.append(film_class);

    }
};

function file_search() {
    let file = document.getElementById('fileName');
    let xhr = new XMLHttpRequest();
    let json = JSON.stringify({
      'film': file.value
    });

    xhr.open('POST', 'http://127.0.0.1:5000/files/', false);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
    xhr.send(json);

    if(xhr.status !== 200) {
        alert('Ошибка соединения с сервером');
    }

    const data = JSON.parse(xhr.responseText);

    alert(data.message);

}

function magnet_search(){
    let magnet = document.getElementById('magnet');
    let xhr = new XMLHttpRequest();
    let json = JSON.stringify({
        'magnet': magnet.value
    });

    xhr.open('POST', 'http://127.0.0.1:5000/download/', false);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
    xhr.send(json);

    if(xhr.status !== 200) {
        alert('Ошибка соединения с сервером');
    }
}
