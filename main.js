//DOM variable
//artist inputs
var artist_1 = document.getElementById('input-artists-1');
var artist_2 = document.getElementById('input-artists-2');
var artist_3 = document.getElementById('input-artists-3');
var artist_4 = document.getElementById('input-artists-4');
var artist_5 = document.getElementById('input-artists-5');
//genre inputs
var genres_1= document.getElementById('input-genres-1');
var genres_2= document.getElementById('input-genres-2');
var genres_3= document.getElementById('input-genres-3');
//track inputs
var songs_1 = document.getElementById('input-songs-1');
var songs_2 = document.getElementById('input-songs-2');
var songs_3 = document.getElementById('input-songs-3');
var songs_4 = document.getElementById('input-songs-4');
var songs_5 = document.getElementById('input-songs-5');
//Submit button
var submit = document.getElementById('submit');

//Store submission
function store(){
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
    
    for (var i=0;i<artists.length;i++){
        artists[i]=artists[i].toLowerCase();
    }
    for (var j=0;j<genres.length;j++){
        genres[j]=genres[j].toLowerCase();
    }
    for (var k=0;k<songs.length;k++){
        songs[k]=songs[k].toLowerCase();
    }
    
    console.log(artists, genres, songs);
    return artists, genres, songs;
}
submit.addEventListener('click', store);