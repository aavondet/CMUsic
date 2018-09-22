//DOM variable
//artist inputs
var artist_1 = document.getElementById('input-artists-1');
var artist_2 = document.getElementById('input-artists-2');
var artist_3 = document.getElementById('input-artists-3');
var artist_4 = document.getElementById('input-artists-4');
var artist_5 = document.getElementById('input-artists-5');
//genre inputs
var genres_1 = document.getElementById('input-genres-1');
var genres_2 = document.getElementById('input-genres-2');
var genres_3 = document.getElementById('input-genres-3');
//track inputs
var songs_1 = document.getElementById('input-songs-1');
var songs_2 = document.getElementById('input-songs-2');
var songs_3 = document.getElementById('input-songs-3');
var songs_4 = document.getElementById('input-songs-4');
var songs_5 = document.getElementById('input-songs-5');
//id
var andrewId = document.getElementById('andrewId');
//Submit button
var submit = document.getElementById('submit');

//Store submission
function store() {
    var artists = [];
    var genres = [];
    var songs = [];

    artists.push(artist_1.value);
    artists.push(artist_2.value);
    artists.push(artist_3.value);
    artists.push(artist_4.value);
    artists.push(artist_5.value);

    genres.push(genres_1.value);
    genres.push(genres_2.value);
    genres.push(genres_3.value);

    songs.push(songs_1.value);
    songs.push(songs_2.value);
    songs.push(songs_3.value);
    songs.push(songs_4.value);
    songs.push(songs_5.value);

    for (var i = 0; i < artists.length; i++) {
        artists[i] = artists[i].toLowerCase();
    }
    for (var j = 0; j < genres.length; j++) {
        genres[j] = genres[j].toLowerCase();
    }
    for (var k = 0; k < songs.length; k++) {
        songs[k] = songs[k].toLowerCase();
    }

    localStorage.setItem("id", andrewId.value);
    // window.location.replace('/result');
    // return artists, genres, songs;

    //send info
    var url = 'http://127.0.0.1:5000/submit';
    var data = {
        "id": andrewId.value,
        "artist_list": artists,
        "genre_list": genres,
        "song_list": songs
    }
    console.log(JSON.stringify(data));
    
     fetch(url, {
         method: 'POST', // or 'PUT'
         body: JSON.stringify(data),
         mode: 'cors',
         headers: {
             'Content-Type': 'application/json; charset=utf-8'
         }
     })
         .then(res => {return res.json()})
         .then(response => console.log('Success:', JSON.stringify(response)))
         .catch(error => console.error('Error:', error));

    // var http = new XMLHttpRequest();
    // http.open('POST', url, true);

    // //Send the proper header information along with the request
    // http.setRequestHeader('Content-type', 'application/json');

    // http.onreadystatechange = function () {//Call a function when the state changes.
    //     if (http.readyState == 4 && http.status == 200) {
    //         alert(http.responseText);
    //     }
    // }
    // http.send(data);
}
//event listeners
// submit.addEventListener('click', () => store);

window.addEventListener('keypress', function (e) {
    var key = e.which || e.keyCode;
    if (key === 13) {
        var artists = [];
        var genres = [];
        var songs = [];

        artists.push(artist_1.value);
        artists.push(artist_2.value);
        artists.push(artist_3.value);
        artists.push(artist_4.value);
        artists.push(artist_5.value);

        genres.push(genres_1.value);
        genres.push(genres_2.value);
        genres.push(genres_3.value);

        songs.push(songs_1.value);
        songs.push(songs_2.value);
        songs.push(songs_3.value);
        songs.push(songs_4.value);
        songs.push(songs_5.value);

        for (var i = 0; i < artists.length; i++) {
            artists[i] = artists[i].toLowerCase();
        }
        for (var j = 0; j < genres.length; j++) {
            genres[j] = genres[j].toLowerCase();
        }
        for (var k = 0; k < songs.length; k++) {
            songs[k] = songs[k].toLowerCase();
        }

        localStorage.setItem("id", andrewId.value);
        console.log(artists, genres, songs);
        // window.location.replace('/result');
        return artists, genres, songs;
    }
});

